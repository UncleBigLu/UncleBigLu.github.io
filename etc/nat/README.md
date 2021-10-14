配置nat将一台未联网设备通过一台已联网设备使用以太网线接入网络。

本次实验将macos作为未联网设备，树莓派作为联网设备，树莓派通过wifi接入网络。

1. 将需联网设备与已联网设备的以太网口配置在同一网段下

   E.g：192.168.10.1/24，192.168.10.2/24

   注意，配置的两个ip不能与已经存在的ip冲突

2. 为需联网机器添加一条默认路由表项

   `sudo route -n add -net default 192.168.10.1`

3. 启动以联网机器的转发功能

   `echo 1 > /proc/sys/net/ipv4/ip_forward`

4. 启动已联网机器的nat转发

   `iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE`

5. 在未联网机器上进行ping测试网络是否联通

   `ping 8.8.8.8`

   