# 自动证书续命

## Install certbot

` sudo python3 -m venv /opt/certbot/` 

`sudo /opt/certbot/bin/pip install --upgrade pip`

` sudo /opt/certbot/bin/pip install certbot`

## Install dnspod plugin

`sudo /opt/certbot/bin/pip3 install certbot-dns-dnspod`

## dnspod插件配置

新建`/etc/certbot-dns-dnspod.ini`,写入

```plaintext
certbot_dns_dnspod:dns_dnspod_email = "email@email.com"
certbot_dns_dnspod:dns_dnspod_api_token = "xxxxx,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

其中dnspod_api_token为dnspod密钥,在DNSPOD官网获取，格式为`ID,Token`

## 实现证书更新后nginx自动重新加载

编辑`/etc/letsencrypt/cli.ini`



加入：

```
deploy-hook = systemctl reload nginx
```

### 申请证书

```
certbot certonly -a certbot-dns-dnspod:dns-dnspod --certbot-dns-dnspod:dns-dnspod-credentials /etc/certbot-dns-dnspod.ini -d bbs.scumaker.org
```

按提示按需回答问题即可。

### 测试renew

```
certbot renew --dry-run
```

期望输出：

```
root@bbs-scumaker:/etc/nginx/sites-enabled# certbot renew --dry-run
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/bbs.scumaker.org.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator certbot-dns-dnspod:dns-dnspod, Installer None
Renewing an existing certificate
Dry run: skipping deploy hook command: systemctl reload nginx

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed without reload, fullchain is
/etc/letsencrypt/live/bbs.scumaker.org/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates below have not been saved.)

Congratulations, all renewals succeeded. The following certs have been renewed:
  /etc/letsencrypt/live/bbs.scumaker.org/fullchain.pem (success)
  /etc/letsencrypt/live/zt.scumaker.org/fullchain.pem (success)
** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates above have not been saved.)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
```

如果遇到错误输出：

```
Renewal configuration file /etc/letsencrypt/renewal/xxx.conf (cert: xxx) produced an unexpected error: 'Namespace' object has no attribute 'certbot_dns_dnspod:dns_dnspod_credentials'. Skipping.
```

