# Mac OS部分操作记录

## 通过proxychains使命令行流量走代理：

1. 通过homebrew安装proxy chains-ng:

`brew install proxy chains-ng`

2. Homebrew安装brew, 其配置文件默认路径为/usr/local/etc/proxychains.conf

```
$ cat /usr/local/etc/proxychains.conf 
# proxychains.conf  VER 4.x
#
#        HTTP, SOCKS4a, SOCKS5 tunneling proxifier with DNS.


# The option below identifies how the ProxyList is treated.
# only one option should be uncommented at time,
# otherwise the last appearing option will be accepted
#
#dynamic_chain
#
# Dynamic - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped)
# otherwise EINTR is returned to the app
#
strict_chain
#
# Strict - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# all proxies must be online to play in chain
# otherwise EINTR is returned to the app
#
#round_robin_chain
#
# Round Robin - Each connection will be done via chained proxies
# of chain_len length
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped).
# the start of the current proxy chain is the proxy after the last
# proxy in the previously invoked proxy chain.
# if the end of the proxy chain is reached while looking for proxies
# start at the beginning again.
# otherwise EINTR is returned to the app
# These semantics are not guaranteed in a multithreaded environment.
#
#random_chain
#
# Random - Each connection will be done via random proxy
# (or proxy chain, see  chain_len) from the list.
# this option is good to test your IDS :)

# Make sense only if random_chain or round_robin_chain
#chain_len = 2

# Quiet mode (no output from library)
#quiet_mode

# Proxy DNS requests - no leak for DNS data
proxy_dns 

# set the class A subnet number to use for the internal remote DNS mapping
# we use the reserved 224.x.x.x range by default,
# if the proxified app does a DNS request, we will return an IP from that range.
# on further accesses to this ip we will send the saved DNS name to the proxy.
# in case some control-freak app checks the returned ip, and denies to 
# connect, you can use another subnet, e.g. 10.x.x.x or 127.x.x.x.
# of course you should make sure that the proxified app does not need
# *real* access to this subnet. 
# i.e. dont use the same subnet then in the localnet section
#remote_dns_subnet 127 
#remote_dns_subnet 10
remote_dns_subnet 224

# Some timeouts in milliseconds
tcp_read_time_out 15000
tcp_connect_time_out 8000

### Examples for localnet exclusion
## localnet ranges will *not* use a proxy to connect.
## Exclude connections to 192.168.1.0/24 with port 80
# localnet 192.168.1.0:80/255.255.255.0

## Exclude connections to 192.168.100.0/24
# localnet 192.168.100.0/255.255.255.0

## Exclude connections to ANYwhere with port 80
# localnet 0.0.0.0:80/0.0.0.0

## RFC5735 Loopback address range
## if you enable this, you have to make sure remote_dns_subnet is not 127
## you'll need to enable it if you want to use an application that 
## connects to localhost.
# localnet 127.0.0.0/255.0.0.0

## RFC1918 Private Address Ranges
# localnet 10.0.0.0/255.0.0.0
# localnet 172.16.0.0/255.240.0.0
# localnet 192.168.0.0/255.255.0.0

# ProxyList format
#       type  ip  port [user pass]
#       (values separated by 'tab' or 'blank')
#
#       only numeric ipv4 addresses are valid
#
#
#        Examples:
#
#            	socks5	192.168.67.78	1080	lamer	secret
#		http	192.168.89.3	8080	justu	hidden
#	 	socks4	192.168.1.49	1080
#	        http	192.168.39.93	8080	
#		
#
#       proxy types: http, socks4, socks5
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
# socks4 	127.0.0.1 9050

```

注释掉最后一行sock4代理，添加自己的代理：

`socks5 127.0.0.1 1080`

**根据代理服务器端口不同调整上述数值*

之后通过`curl cip.cc`检查自己的ip查看是否生效：

`proxychains4 curl cip.cc`

我的系统在键入此命令后显示已经为代理服务器ip。但参考[其它博客](https://www.jianshu.com/p/123638a60704)得知可能存在仍然无法代理流量情况：

```
[proxychains] config file found: /usr/local/etc/proxychains.conf
[proxychains] preloading /usr/local/Cellar/proxychains-ng/4.14/lib/libproxychains4.dylib
IP  : 114.***.***.148
地址  : 中国  XX
运营商 : 电信

数据二 : XX市XX区 | 电信

数据三 : 中国XX省XX市 | 电信

URL : http://www.cip.cc/114.***.***.148
```

*以下内容转载于博客：https://www.jianshu.com/p/123638a60704*

发现没有任何用，为啥呢？因为我用的是万恶的Mac。
 macOS 10.11 后下由于开启了 SIP（System Integrity Protection） 会导致命令行下 proxychains-ng 代理的模式失效，如果使用 proxychains-ng 这种简单的方法，就需要先关闭 SIP。

### 关闭 SIP

重启Mac，按住⌘ + R进入Recovery模式。 实用工具（Utilities）-> 终端（Terminal）。 输入命令csrutil disable运行。 重启进入系统后，终端里输入 csrutil status，结果中如果有 System Integrity Protection status:disabled. 则说明关闭成功。



```undefined
➜  ~ csrutil status
System Integrity Protection status: disabled.
➜  ~
```

我们再试一次：



```csharp
➜  ~ proxychains4 curl cip.cc
[proxychains] config file found: /usr/local/etc/proxychains.conf
[proxychains] preloading /usr/local/Cellar/proxychains-ng/4.14/lib/libproxychains4.dylib
[proxychains] DLL init: proxychains-ng 4.14
[proxychains] Random chain  ...  127.0.0.1:1086  ...  106.***.206.***:80  ...  OK
IP  : ***.112.***.116
地址  : 美国  美国

数据二 : 美国 | Amazon EC2服务器

数据三 : 美国华盛顿 | 亚马逊

URL : http://www.cip.cc/***.112.***.116
```

出现上述界面说明proxychains已正常工作。之后仅需使用`proxychains4 <所需走代理的命令>`即可使命令流量走代理。

Eg：`proxychains4 git clone  git@github.com:torvalds/linux.git`

 