# Zerotier

## 使用zerotier自组虚拟局域网

## 何为虚拟局域网

VLAN（Virtual Local Area Network）的中文名为"虚拟局域网"。 
虚拟局域网（VLAN）是一组逻辑上的设备和用户，这些设备和用户并不受物理位置的限制，可以根据功能、部门及应用等因素将它们组织起来，相互之间的通信就好像它们在[同一个网段](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BD%91%E6%AE%B5/10612240)中一样，由此得名虚拟局域网。VLAN是一种比较新的技术，工作在[OSI参考模型](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/OSI%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B)的第2层和第3层，一个VLAN就是一个[广播域](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E5%B9%BF%E6%92%AD%E5%9F%9F/5293530)，VLAN之间的通信是通过第3层的[路由器](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E8%B7%AF%E7%94%B1%E5%99%A8/108294)来完成的。与传统的[局域网技术](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E5%B1%80%E5%9F%9F%E7%BD%91%E6%8A%80%E6%9C%AF/2597024)相比较，VLAN技术更加灵活，它具有以下优点： 网络设备的移动、添加和修改的管理开销减少；可以控制[广播](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E5%B9%BF%E6%92%AD/656406)活动；可提高[网络](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E7%BD%91%E7%BB%9C/143243)的安全性。
在计算机网络中，一个二层网络可以被划分为多个不同的广播域，一个广播域对应了一个特定的用户组，默认情况下这些不同的广播域是相互隔离的。不同的广播域之间想要通信，需要通过一个或多个路由器。这样的一个广播域就称为VLAN。

## 何为zerotier

ZeroTier将整个世界转变为单个数据中心或云区域。 将所有设备，虚拟机和应用程序联接起来，就像在同一个交换机接入所有设备一样。

简单来说, 它就是一个VLAN组建工具, 不过与一般的组建VLAN的工具(如Hamachi, n2n等)不同, ZeroTier有这么几个优势:

- **几乎零配置**: 传统的VLAN组建工具一般都需要自建超级结点(如n2n的supernode), 需要在一台有公网ip的服务器上进行一系列的配置, 整体来说对新手比较劝退.
- **可以固定自定义ip**: 这一点相对于Hamachi, 通过自建的网络, 我们可以自定义一个固定的ip, 你可以, 用192.168.1.1来访问云服务器1,  用192.168.1.2来访问云服务器2, 方便记忆, 而不是像Hamachi一样生成类似5.233.212.45这样的随机ip.
- **跨平台**: ZeroTier提供了windows, macOS, linux, Android, iOS...几乎全平台的客户端, 你可以把任意平台的设备接入VLAN.

## 下载并配置zerotier

### 创建zerotier帐号则肉体而

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

![netmanagement](/home/lu/Desktop/repository/UncleBigLu.github.io/etc/zerotier/img/netmanagement.png)交互

你应当能在这里看到你刚刚加入的设备。勾选Auth？栏单选框以正式将节点加入网络。

## 检测网络是否正常运行

在不同的设备上按上述步骤操作，将需要相互通信的设备加入到同一网络内。

多个设备加入网络后，即可使用zerotier分配到的局域网ip地址进行相互通信

运行ping指令以确定网络是否连通，连通后即可使用局域网下通信方式进行数据交互交互。

