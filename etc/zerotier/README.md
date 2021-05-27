# Zerotier

## 使用zerotier自组虚拟局域网

### 创建zerotier帐号

登录zerotier官网并[创建帐号](https://accounts.zerotier.com/auth/realms/zerotier/protocol/openid-connect/registrations?client_id=zt-central&redirect_uri=https%3A%2F%2Fmy.zerotier.com%2Fapi%2F_auth%2Foidc%2Fcallback&response_type=code&scope=all&state=state)

### 登录帐号并新建网络

访问[登录页面](https://accounts.zerotier.com/auth/realms/zerotier/protocol/openid-connect/auth?client_id=zt-central&redirect_uri=https%3A%2F%2Fmy.zerotier.com%2Fapi%2F_auth%2Foidc%2Fcallback&response_type=code&scope=all&state=state)并使用之前创建的帐号登录。

![ztnewnet](/home/lu/Desktop/repository/UncleBigLu.github.io/etc/zerotier/img/ztnewnet.png)

单击Create A Network来创建一个网络

![network](/home/lu/Desktop/repository/UncleBigLu.github.io/etc/zerotier/img/network.png)

### 联通为对应设备下载zerotier客户端

[官方网站下载链接](https://www.zerotier.com/download/)

要在树莓派raspberrypi os上部署zerotier，终端运行以下指令

`curl -s https://install.zerotier.com | sudo bash`

### 检查下载是否成功

树莓派终端运行`zerotier-cli info`

![nodeinfo](/home/lu/Desktop/repository/UncleBigLu.github.io/etc/zerotier/img/nodeinfo.png)

出现此输出证明下载成功。其中第三项即为你的设备id

### 加入网络

1. 记录下你刚刚创建的网络id
2. 树莓派终端运行`zerotier-cli join ################`, ################为你要加入的16为网络ID
3. 登录zerotier官网并单击网络进入管理界面

![netmanagement](/home/lu/Desktop/repository/UncleBigLu.github.io/etc/zerotier/img/netmanagement.png)

你应当能在这里看到你刚刚加入的设备。勾选Auth？栏单选框以正式将节点加入网络。

## 检测网络是否正常运行

多个设备加入网络后，即可使用zerotier分配到的局域网ip地址进行相互通信

运行ping指令以确定网络是否连通。

