# linux basic usage and commands

查看系统版本：`lsb_release -a`

查看系统架构： `uname -a`

列出已安装软件包： `apt list --installed` 。本命令显示使用apt安装的所有软件包及由于被依赖而安装的包

查找源软件包：`apt-get search`


### git clone 走代理：
添加文件~/.ssh/config：
Host github.com
ProxyCommand=nc -X 5 -x 127.0.0.1:1080 %h %p
(127.0.0.1为代理端口)

如果想全部走代理就把Host github.com 换成 Host *
详见
https://gist.github.com/bynil/2126e374db8495fe33de2cbc543149ae



### 好用的代理管理工具：FoxyProxy

### 命令与文件的查询
#### 脚本文件名查询：which
`which [-a] command`  -a 列出所有PATH中可以找到的命令，而不是只有第一个被找到的命令名称。

#### 文件名查找

**whereis**寻找特定文件

`whereis [-bmsu] 文件或目录名`

**locate**

`locate [-ir] keyword` -i ：忽略大小写差异  -r：后面可接正则表达式。

本命令可直接输入”文件的部分名称“进行查找。

**find**

`find [PATH] [option] [action]`












