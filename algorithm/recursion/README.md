# 递归和分治

## 合并排序

### 基本思想：

将待排序元素从中间分开，分别对两个子集进行排序，再将两个子集合并。

### 复杂度：
T(n) = O(nlogn)

### 代码：

```c++
void merge(int *a, int start, int mid, int end)
{
    int len_f = mid - start + 1;
    int len_b = end - mid;
    int buf_f[len_f], buf_b[len_b];

    for(int i = 0; i < len_f; ++i)
    {
        buf_f[i] = a[start + i];
    }
    for(int i = 0; i < len_b; ++i)
    {
        buf_b[i] = a[mid + i + 1];
    }

    int i = 0, j = 0, cnt = 0;
    while(i < len_f && j < len_b)
    {
        if(buf_f[i] < buf_b[j])
        {
            a[start + cnt] = buf_f[i++];
        }
        else
        {
            a[start + cnt] = buf_b[j++];
        }
        ++cnt;
    }
    while(i < len_f)
    {
        a[start + cnt] = buf_f[i++];
        ++cnt;
    }
    while(j < len_b)
    {
        a[start + cnt] = buf_b[j++];
        ++cnt;
    }
}

void mergeSort(int *a, int start, int end)
{
    if(start < end)
    {
        int mid = (start + end) / 2;
        mergeSort(a, start, mid);
        mergeSort(a, mid+1, end);
        merge(a, start, mid, end);
    }
}
```

### 快速排序

#### 基本思想：

从数组中任取一个数作为中间数，将小于该数的元素全部移动到该元素左边，大于的全部移动到右边，之后再对两边分别进行排序。

```c++
int partition(int* arr, int begin, int end)
{
    int last_attr_pos = end - 1;
    int pivot = arr[last_attr_pos];

    /*
     * Assume i equals to correct pivot position, and all attributes
     * in the array bigger pivot, so i = 1 at the first. Scan the whole
     * array, if found an element e less than pivot, then swap e and arr[i]
     * and ++i(move the small element to the left and shift right
     * the correct pivot position). Finally, move the pivot element to the
     * correct position.
     * */
    int i = begin;
    for(int j = begin; j < last_attr_pos; ++j)
    {
        if(arr[j] < pivot)
        {
            std::swap(arr[i], arr[j]);
            ++i;
        }
    }
    std::swap(arr[i], arr[last_attr_pos]);
    return i;
}

void fast_sort(int *a, int begin, int end)
{
    if(begin == end - 1)
        return;
    int mid = partition(a, begin, end);
    fast_sort(a, begin, mid);
    fast_sort(a, mid, end);
}
```

