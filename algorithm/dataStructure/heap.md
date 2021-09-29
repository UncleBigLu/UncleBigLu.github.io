# 堆

## 定义

堆分为最小堆和最大堆，结构上为完全二叉树（但我们可以用数组去储存堆，后面会讲到）。

最小堆中，每个元素均小于它的子节点，根为整棵树的最小值。最大堆相反。

## 数组储存堆

```c++
parent = (index-1) / 2
leftChild = index*2 + 1
rightChild = index*2 + 2
```

parent = (index-1) / 2

leftChild = index*2 + 1

# 堆操作

操作以最小堆进行举例。

```c++
void heapifyUp() {
  int index = size - 1;
  while (hasParent(index) && parent(index) > arr[index]) {
    std::swap(arr+getParentIndex(index), arr+index);
  }
}

void heapifyDown(int index) {
  while(hasLeftChild(index)) {
    int smallerChildIndex = getLeftChildIndex(index);
    if(hasRightChild(index) && rightChild(index) < leftChild(index)) {
      smallerChildIndex = getRightChildIndex(index);
    }
    if(arr[index] > arr[smallerChildIndex]) {
      std::swap(arr+index, arr+smallerChildIndex);
    }
    else{
      break;
    }
    index = smallerChildIndex;
  }
}
```

## 建堆

虽然向现有堆中插入元素复杂度为log(n), 但建堆可以以o(n)的复杂度完成。原因在于插入元素使用的方法是heapifyUp(), 而建堆使用的方法为heapifyDown.（二叉树下方元素大于上方元素，将所有元素下移显然比将所有元素上移开销要小）

```c++
/*
	首先将所有元素随便建成完全二叉树，之后再从这棵树上从下往上建成堆
*/
void buildHeap(){
  // Index of last non-leaf node
  int startIdx = (heap_size / 2) - 1;
  
  for (int i = startIdx; i >= 0; --i){
    heapifyDown(i);
  }
}
```



### 分析

算法本质上为从最下方开始，将每一棵子树建成堆。每次执行heapifyDown时，当前节点的两个子树均为堆。



## 插入

每次插入均插入在最后一个元素。若元素不满足堆的限制条件，则将其上移直到堆的限制条件成立。即将插入的节点与其父节点比较，若父节点>新节点，则交换两者并继续这一过程。

```c++
void add(int item) {
  arr[size++] = item;
  heapifyUp();
}
```

## 删除堆顶

删除堆顶后，将最后一个元素移动至堆顶，之后将它与子节点中较小的那个交换，重复这一过程。

```c++
int pop() {
  if(heap_size == 0) error();
  
  int ret = arr[0];
 	arr[0] = arr[heap_size - 1];
  --heap_size;
  heapifyDown(0);
  return ret;
}
```

## 

