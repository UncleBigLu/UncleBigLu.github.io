# database

## Linux 上服务器PostgreSQL:

#### 启动服务器：

`sudo -i -u postgres`, 或`sudo -i -u postgres psql`直接进入PostgreSQL命令窗口。

**Note: pgsql用分号标记结尾，语句最后记得加分号**

#### 创建数据库

`CREATE DATABASE <dbname>`

#### 选择数据库

在命令窗口中输入以下内容：

\l: 显示已经存在的数据库

`postgres=# \l`

进入数据库：

`postgres=# \c dbname`

#### 在Postsql命令窗口下执行命令：

用文本编辑器将多条SQL语句完整写好后存为.sql文件，再用\i命令执行。

`\i <filename>`

#### 显示已有表格：

`dbname=# \d`

#### 删除表格

`DROP TABLE <table_name>`





