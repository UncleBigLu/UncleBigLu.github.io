# Deploy gstreamer on raspberrypi

本次部署使用硬件为Raspberrypi 3 Model B+, 使用系统镜像为2021-01-11-raspios-buster-armhf-lite.img

## 部署前步骤

### 树莓派apt包管理器换源

使用镜像站为科大镜像站。具体操作步骤如下：

```
# 编辑 `/etc/apt/sources.list` 文件，删除原文件所有内容，用以下内容取代：
deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ buster main contrib non-free rpi
# deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ buster main contrib non-free rpi

# 编辑 `/etc/apt/sources.list.d/raspi.list` 文件，删除原文件所有内容，用以下内容取代：
deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ buster main ui
#deb-src http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ buster main ui

```

执行完成后运行`sudo apt-get update`

## 部署gstreamer

### apt-get下载

```
sudo apt-get install gstreamer1.0-tools gstreamer1.0-omx gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gtk-doc-tools

```

### clone gst-rtsp-server 代码仓库

`git clone https://github.com/GStreamer/gst-rtsp-server.git`

### 根据gst版本源码编译gst-rtsp-server

`apt show gstreamer1.0-tools`

在我这里的输出为

```
Package: gstreamer1.0-tools
Version: 1.14.4-1
Priority: optional
Section: utils
Source: gstreamer1.0
Maintainer: Maintainers of GStreamer packages <gstreamer1.0@packages.debian.org>
Installed-Size: 1196 kB
Depends: libc6 (>= 2.7), libglib2.0-0 (>= 2.40), libgstreamer1.0-0 (>= 1.14.3)
Suggests: gstreamer1.0-plugins-base
Homepage: https://gstreamer.freedesktop.org
Download-Size: 1109 kB
APT-Manual-Installed: yes
APT-Sources: https://mirrors.ustc.edu.cn/raspbian/raspbian buster/main armhf Packages
Description: Tools for use with GStreamer
 GStreamer is a streaming media framework, based on graphs of filters
 which operate on media data.  Applications using this library can do
 anything from real-time sound processing to playing videos, and just
 about anything else media-related.  Its plugin-based architecture means
 that new data types or processing capabilities can be added simply by
 installing new plug-ins.
 .
 This package contains versioned command-line tools for GStreamer.

```

版本为1.14.4， 将gst-rtsp-server1.14.4版本进行源码编译

```
cd gst-rtsp-server
git checkout 1.14.4
./autogen.sh
make
```

## 验证输出

在树莓派上安装csi摄像头并启动，运行以下命令

```
cd examples
raspivid -n -w 1280 -h 720 -b 1000000 -fps 30 -t 0 -o - | ./test-launch "( fdsrc ! h264parse ! rtph264pay name=pay0 pt=96 )" -p 5600 --gst-debug-level=3

```

即可在树莓派5600端口读取到rtsp视频流输出。演示图像如下：

![result](/home/lu/Desktop/repository/UncleBigLu.github.io/linux_notes/rpi_notes/gstreamer/img/result.png)