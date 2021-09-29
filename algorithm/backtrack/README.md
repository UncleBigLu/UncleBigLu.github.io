# 回溯法

本质上是一种组织的井井有条的穷举搜索。

按深度优先搜索。搜索到任一节点时，根据限制条件对解空间树进行剪枝，避免不必要的搜索。

## 部分定义

### 扩展节点

一个正在产生儿子的结点称为扩展结点

### 活节点

一个自身已生成但其儿子还没有全部生成的节点称做活结点

### 死节点

一个所有儿子已经产生的结点称做死结点

### 回溯法

回溯法：为了避免生成那些不可能产生最佳解的问题状态，要不断地利用限界函数(bounding function)来处死那些实际上不可能产生所需解的活结点，以减少问题的计算量。具有限界函数的深度优先生成法称为回溯法
