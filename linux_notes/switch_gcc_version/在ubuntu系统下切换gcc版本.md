# 在ubuntu系统下切换gcc版本

**Eg：由gcc9切换至gcc7**

### Step1：查看现有gcc版本。

`gcc -v`

### Step2：查看是否已有gcc7（目标）版本。

`ls /usr/bin/gcc*`

如果没有内容，用`whereis`命令找到gcc位置。

### Step3：下载目标版本。如果你已有目标版本，跳转至第四步。

```bash
sudo apt-get update
apt-cache search gcc-7
sudo apt-get install gcc-7
```

### Step4：配置gcc版本

`sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 50`

`sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 40`

上述指令作用：

```
 --install link name path priority [--slave link name path]...
              Add  a group of alternatives to the system.  link is the generic
              name for the master link, name is the name of its symlink in the
              alternatives  directory,  and  path  is  the  alternative  being
              introduced for the master link.  The arguments after --slave are
              the generic name, symlink name in the alternatives directory and
              the alternative path for a slave link.   Zero  or  more  --slave
              options,  each  followed  by  three arguments, may be specified.
              Note that the master alternative must exist  or  the  call  will
              fail.   However  if  a  slave  alternative  doesn't  exist,  the
              corresponding  slave  alternative  link  will  simply   not   be
              installed (a warning will still be displayed). If some real file
              is installed where an alternative link has to be  installed,  it
              is kept unless --force is used.

```

之后运行`sudo update-alternatives --config gcc`

得到下列输出

```
Selection    path               Priority    Status
--------------------------------------------------------------------
* 0          /usr/bin/gcc-7   50          auto mode
  1          /usr/bin/gcc-7   50          manual mode
  2          /usr/bin/gcc-9   40          manual mode
```

显示配置完成，按下回车确认即可，或输入序号选择需要的版本。

#### fin

### note：

如果你需要删除某个版本，

`sudo update-alternatives --remove gcc /usr/bin/gcc-7`



