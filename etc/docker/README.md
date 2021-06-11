# Docker

## docker architecture

Docker uses a client-server architecture. The Docker *client* talks to the Docker *daemon*, which does the heavy lifting of building, running, and distributing your Docker containers. 

## docker objects

### images

只读模版，用于创建container.

### container

image的可运行实例。

A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state.

## commands

| commands | Description |
| ------------------------------------------------------------ | --------------------------------------------- |
| [docker ps](https://docs.docker.com/engine/reference/commandline/ps/) | List containers                               |
| [docker pull](https://docs.docker.com/engine/reference/commandline/pull/) | Pull an image or a repository from a registry |
| [docker image](https://docs.docker.com/engine/reference/commandline/image/) | Manage images |
| [docker images](https://docs.docker.com/engine/reference/commandline/images/) | List images   |
| [docker run](https://docs.docker.com/engine/reference/commandline/run/) | Run a command in a new container |
| [docker exec](https://docs.docker.com/engine/reference/commandline/exec/) | Run a command in a running container |                   |
| [docker kill](https://docs.docker.com/engine/reference/commandline/kill/) | Kill one or more running containers |
| [docker container](https://docs.docker.com/engine/reference/commandline/container/) | Manage containers |

### 常用命令

`docker exec -it <container> <command>`	// --interactive, Keep STDIN open even if not attached	--tty allocate a pseudo-TTY

`Eg: docker exec -it CONTAINER_NAME /bin/bash 	//Create a new Bash session in container`

删除container: `docker rm <container>`

显示container log：`docker logs <container>`



## docker deploy mysql

```
docker pull mysql
# Create directory for mysql container to store data
mkdir /var/lib/docker-mysql
# --name: container name
# -v: Set docker volume. 
# -e: use environment variables to set sql passwd
# -d, --detach: Run container in background and print container id
# -p: map docker port to host port
sudo docker run --name mysql -v /var/lib/docker-mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysqlPasswd -p 3306:3306 -d mysql
# Note: 3306 is mysql default port
```



