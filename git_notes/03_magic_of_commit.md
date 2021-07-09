# 多分支管理

## 深究commit

![commit objects](https://git-scm.com/book/en/v2/images/data-model-3.png)

[Git对象库](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)

- 对改动过的文件整体做校验值，并生成 *校验值-diff* 键值对。存储在`.git/objects/`目录下。
- commit以链表式存储。新的commit会存储父commit的校验值。
- commit存储该提交时的文件树对象的指针（另一个指针集合）
- 文件树对象储存了对应的文件指针

### 思考

- 为什么后端实现完全不存文件diff？
- 使用git时候的Best Practical？

## 分支？

- 使一个仓库能够拥有多个可以同时向前推进的世界线。
- 其实只储存了这条世界线最新的commit校验值。

