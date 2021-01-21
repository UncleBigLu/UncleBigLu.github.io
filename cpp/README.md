# c++与算法知识点记录

## STL

### 排序与检索：

#### std::sort

使用sort需要`#include <algorithm>`

```c++
template <typename RandomAccessIterator>
	void sort (RandomAccessIterator first, RandomAccessIterator last);
```

对排序对象进行升序排序。其排序依赖于 **<** 运算符

Eg: 对数组a[5]进行排序：`sort(a, a+5)`

*ps:还有另一个手动传入排序函数的sort版本未在此记录。*

#### 二分查找

```c++
std::lower_bound()
std::upper_bound()
std::binary_search()
```

分别返回待查找值的下界，上界。binary_search返回值是否存在。

```c++
template <typename FowardIterator, typename T>
	ForwardIterator lower_bound(ForwardIterator first, ForwardIterator last, 
                             const T& val);
```

Eg: 查找x在数组a中下界的下标：

```c++
int pos = lower_bound(a, a + a_lenth, x) - a;
```

*ps:还有另一个手动传入排序函数的二分查找版本未在此记录。*



### Std::set

Set 中元素已从小到大排序，且相同元素仅出现一次。

set中元素一旦插入后不允许修改，但允许删除和插入新元素。



### std::map

key到value的映射。

Eg: string为键int为值的map：`map<string, int> m;`



