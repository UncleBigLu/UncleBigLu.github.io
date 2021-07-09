# Nginx

## conf.d

To make the configuration easier to maintain, we recommend that you split it into a set of feature‑specific files stored in the **/etc/nginx/conf.d** directory and use the [`include`](https://nginx.org/en/docs/ngx_core_module.html#include) directive in the main **nginx.conf** file to reference the contents of the feature‑specific files.

## Config nginx as web server

### server_name

If there are several servers that match the IP address and port of the request, NGINX Plus tests the request’s `Host` header field against the [`server_name`](https://nginx.org/en/docs/http/ngx_http_core_module.html#server_name) directives in the `server` blocks. The parameter to `server_name` can be a full (exact) name, a wildcard, or a regular expression. A wildcard is a character string that includes the asterisk (`*`) at its beginning, end, or both; the asterisk matches any sequence of characters. NGINX Plus uses the Perl syntax for regular expressions; precede them with the tilde (`~`). This example illustrates an exact name.

可以通过DNS cname将不同的host解析到同一ip（xxx.scumaker.org)

### location

支持正则表达式。

### root

The [`root`](https://nginx.org/en/docs/http/ngx_http_core_module.html#root) directive specifies the file system path in which to search for the static files to serve. The request URI associated with the location is appended to the path to obtain the full name of the static file to serve. In the example above, in response to a request for **/images/example.png**, NGINX Plus delivers the file **/data/images/example.png**.

### try_files

可用于判断文件或目录是否存在，不存在情况下重定向或返回http status code。

