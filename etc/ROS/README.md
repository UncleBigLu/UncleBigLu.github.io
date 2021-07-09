# ROS

## Deploy ros in docker

> The environment of this tutorial is Ubuntu 20.04, with docker installed.

### Using ROS iamges

` docker pull ros`

This command would pull ROS foxy distribution. To install other version of ROS, check [this tutorial](http://wiki.ros.org/docker/Tutorials/Docker).

After the pull process finish, run `docker run -it ros` to enter the ros environment. You can run `rosversion -d ` to check your ROS version.

## Run ROS gui in docker

[Reference:  ROS Wiki](http://wiki.ros.org/docker/Tutorials/GUI)

The simple way is expose your xhost so that container can render to the  correct display by reading and writing though the X11 unix socket. 

First we need to adjust the permission of the X server host.

```
xhost +local:root # for the lazy and reckless
```

This is not safe, as it given all process running by root previlege to display on your screen. You should unset the permission after you shutdown your container.

```
xhost -local:root
```

A better option is opening up xhost only to the specific system that you want, for instance if you are running a container on the local host's docker daemon with container's ID stored to the shell variable containerId.

```
xhost +local:`docker inspect --format='{{ .Config.Hostname }}' $containerId`
```

```
docker run -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    ros
```

