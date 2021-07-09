# 翻墙
## GFW
### GFW工作原理？
有GFW情况下：本地计算机发出一个数据包给Google，经由**本地网络**接入**骨干网**，经过DNS解析。由于http为明文，GFW发现访问目的为google后，进行**DNS污染**（解析错误地址或不解析）。同时，其可以进行**关键字阻断**，在包含某些关键字时中断连接。同时，GFW也可在某些特定IP的服务器的主机的特定端口进行端口阻断，切断VPN或SSL链接。同时，GFW可以对被记录的IP地址进行批量封锁。总结：

- DNS污染 解析错误地址或不解析
- 过滤关键字
- 端口阻断
- IP地址批量封锁

### VPN翻墙实现方式：
本地网络计算机发送一个请求建立加密通道的数据包 接入骨干网 域名解析 由于该数据包目的地被GFW允许放行，可以到达。数据包经过中转服务器解密出真实想访问的地址，代替访问，并将目标服务器数据转发到本地计算机。

由于数据流量不再是明文，规避了关键字屏蔽。由于访问对象是被允许的服务器，规避了DNS污染。

但这种方式是有**特征**的：先发送一个数据包请求和一个服务器建立加密连接，之后紧跟着一个代理请求。GFW可以对这些有明显特征的流量作出以下处理：1. 屏蔽VPN端口，以后再想用VPN，需要申请报备。2. 积累提供VPN服务的服务器IP，并批量封锁。

### Shadowsocks:
思路：将代理服务器拆分成本地和远程两个，实现经过GFW的流量全部加密，从而消除明显的流量特征。

具体实现： 本地主机发出数据包，交给本地的Shadowsocks服务器（即本地安装的Shadowsocks翻墙软件，或翻墙路由器/软路由等硬件）发送数据加密请求。之后，发送加密数据经过骨干网到达国际出口。由于不包含明显特征，不会被GFW拦截。之后，到达远程中转服务器，进行数据解密并转发到真实目的地。返回的数据也在中转服务器进行加密后再经过GFW，同样无明显特征/不是http明文数据，放行。到达本地Shadowsocks服务器，解密，返回本地主机。



## 过墙方式大致分类

- 软件翻墙
- 硬件翻墙
- 网关模式翻墙

## 线路
### CN2: ChinaNetNextCarryingNetwork 中国电信下一代承载网络
相较老的163骨干网搭载了QoS, 服务质量更好。
QoS：quality of service, 根据服务需求安排流量优先级
CN2价格较高。个人用户较少
购买CN2线路时注意买的是双向CN2还是单向。出国CN2回国163的话仍然会卡....


## 协议特点对照分析
### Shadowsocks
### v2ray websocket+tls
伪装https流量 （但伪装流量目的没有任何网站）。但可以v2ray+websocket+tls+web在v2ray服务外面套一个真的网站。
### trojan
类似websocket+tls，比v2ray更轻量级（但没有vmess，支持的通讯协议是固定的）。仅使用高效tls加密。

## VPN
由于V2RAY等翻墙软件运作在会话层，故无法代理运输在传输层的游戏流量（TCP/UDP）以及运行在网络层的ICMP流量（PING、TRACE..等）。而VPN运作在数据链路层，几乎可以代理所有流量，能够实现真·全局代理。

## 部分较知名机场
薯条 RixCloud 魅影 BlinkLoad 海豚湾 佩奇 aaex



## Local v2ray config

```json
{
	"dns": {
		"hosts": {
			"domain:googleapis.cn": "googleapis.com"
		},
		"servers": [
			"8.8.8.8"
		]
	},
	"inbounds": [
		{
			"listen": "127.0.0.1",
			"port": 8581,
			"protocol": "socks",	// Socks5 protocol
			"settings": {
				"auth": "noauth",
				"udp": true,
				"userLevel": 8
			},
			"sniffing": {
				"destOverride": [
					"http",
					"tls"
				],
				"enabled": true
			},
			"tag": "socks"
		}
	],
	"log": {
		"loglevel": "warning"
	},
	"outbounds": [
		{
			"mux": {
				"concurrency": -1,
				"enabled": false
			},
			"protocol": "vmess",
			"settings": {
				"vnext": [
					{
						"address": "YOUR REMOTE SERVER HOSTNAME",
						"port": 443,
						"users": [
							{
								"alterId": 32,
								"id": "YOUR REMOTE SERVER V2RAY UUID",
								"level": 8,
								"security": "auto"
							}
						]
					}
				]
			},
			"streamSettings": {
				"network": "ws",
				"security": "tls",
				"tlssettings": {
					"allowInsecure": false,
					"serverName": "YOUR REMOTE SERVER HOSTNAME"
				},
				"wssettings": {
					"connectionReuse": true,
					"headers": {
						"Host": "YOUR REMOTE SERVER HOSTNAME"
					},
					"path": "/v2ray"	// Depending on your reverse proxy settings
				}
			},
			"tag": "proxy"
		},
		{
			"protocol": "freedom",
			"settings": {},
			"tag": "direct"
		},
		{
			"protocol": "blackhole",
			"settings": {
				"response": {
					"type": "http"
				}
			},
			"tag": "block"
		}
	],
	"policy": {
		"levels": {
			"8": {
				"connIdle": 300,
				"downlinkOnly": 1,
				"handshake": 4,
				"uplinkOnly": 1
			}
		},
		"system": {
			"statsInboundUplink": true,
			"statsInboundDownlink": true
		}
	},
	"routing": {
		"domainStrategy": "IPIfNonMatch",
		"rules": [
			{
				"ip": [
					"geoip:private"	// Direct connect Lan devices
				],
				"outboundTag": "direct",
				"type": "field"
			},
			{
				"ip":[
					"geoip:cn"	// Direct connect CN websites.
				],
				"outboundTag": "direct",
				"type": "field"
			}
		]
	},
	"stats": {}
}

```

## Remote Server v2ray config

```json
{
	"log": {
		"access": "/var/log/v2ray/access.log",
		"error": "/var/log/v2ray/error.log",
		"loglevel": "warning"
	},
	"inbounds": [
		{
			"listen": "127.0.0.1",
			"port": 45231,	// Reverse proxy the client request to this port
			"protocol": "vmess",
			"settings": {
				"clients": [
					{ "id": "SERVER UUID", "alterId":32, "tag":"atag" }
				]
			},
			"streamSettings": {
				"network": "ws"
			},
			"sniffing": {
				"enabled": true,
				"destOverride": [
					"http",
					"tls"
				]
			}
		}
		//include_ss
		//include_socks
		//include_mtproto
		//include_in_config
		//
	],
	"outbounds": [
		{
			"protocol": "freedom",
			"settings": {
				"domainStrategy": "UseIP"
			},
			"tag": "direct"
		},
		{
			"protocol": "blackhole",
			"settings": {},
			"tag": "blocked"
        }
		//include_out_config
		//
	],
	"dns": {
		"servers": [
			"https+local://cloudflare-dns.com/dns-query",
			"1.1.1.1",
			"1.0.0.1",
			"8.8.8.8",
			"8.8.4.4",
			"localhost"
		]
	},
	"routing": {
		"domainStrategy": "IPOnDemand",
		"rules": [
			{
				"type": "field",
				"ip": [
					"0.0.0.0/8",
					"10.0.0.0/8",
					"100.64.0.0/10",
					"127.0.0.0/8",
					"169.254.0.0/16",
					"172.16.0.0/12",
					"192.0.0.0/24",
					"192.0.2.0/24",
					"192.168.0.0/16",
					"198.18.0.0/15",
					"198.51.100.0/24",
					"203.0.113.0/24",
					"::1/128",
					"fc00::/7",
					"fe80::/10"
				],
				"outboundTag": "blocked"
			}
			,
			{
				"type": "field",
				"domain": [
					"domain:epochtimes.com",
					"domain:epochtimes.com.tw",
					"domain:epochtimes.fr",
					"domain:epochtimes.de",
					"domain:epochtimes.jp",
					"domain:epochtimes.ru",
					"domain:epochtimes.co.il",
					"domain:epochtimes.co.kr",
					"domain:epochtimes-romania.com",
					"domain:erabaru.net",
					"domain:lagranepoca.com",
					"domain:theepochtimes.com",
					"domain:ntdtv.com",
					"domain:ntd.tv",
					"domain:ntdtv-dc.com",
					"domain:ntdtv.com.tw",
					"domain:minghui.org",
					"domain:renminbao.com",
					"domain:dafahao.com",
					"domain:dongtaiwang.com",
					"domain:falundafa.org",
					"domain:wujieliulan.com",
					"domain:ninecommentaries.com",
					"domain:shenyun.com"
				],
				"outboundTag": "blocked"
			}			,
                {
                    "type": "field",
                    "protocol": [
                        "bittorrent"
                    ],
                    "outboundTag": "blocked"
                }
			//include_ban_ad
			//include_rules
			//
		]
	},
	"transport": {
		"kcpSettings": {
            "uplinkCapacity": 100,
            "downlinkCapacity": 100,
            "congestion": true
        }
	}
}

```

## Nginx reverse proxy

```
server
    {
        listen 443 ssl;
				listen [::]:443 ssl;

        server_name     SERVER_NAME;
        ssl_certificate CERT_LOCATION;
        ssl_certificate_key CERT_KEY_LOCATION;

        ssl_protocols TLSv1.2 TLSv1.3; 
        ssl_prefer_server_ciphers on;
	ssl_ciphers HIGH:!aNULL:!MD5;
	add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";

	location /v2ray
	{
	    if ($http_upgrade != "websocket"){
		return 404;
	    }
	    proxy_redirect off;
	    proxy_pass http://localhost:45231/;
	    proxy_set_header Host $host;
	    proxy_set_header Connection "upgrade";	# Use this header to indentify using websocket protocol
	    proxy_set_header Upgrade $http_upgrade;	# Use this header to indentify using websocket protocol
#	    proxy_set_header X-Real-IP $remote_addr;
#            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

	    proxy_buffering off;
	    
	}
	
    }

```

