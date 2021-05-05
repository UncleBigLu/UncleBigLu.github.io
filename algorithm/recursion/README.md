# 递归和分治

## 合并排序

### 基本思想：

将待排序元素从中间分开，分别对两个子集进行排序，再将两个子集合并。

### 复杂度：
T(n) = O(nlogn)

### 代码：

```c++
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;
 
    // Create temp arrays
    int L[n1], R[n2];
 
    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
 
    // Merge the temp arrays back into arr[l..r]
 
    // Initial index of first subarray
    int i = 0;
 
    // Initial index of second subarray
    int j = 0;
 
    // Initial index of merged subarray
    int k = l;
 
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    // Copy the remaining elements of
    // L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    // Copy the remaining elements of
    // R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
// l is for left index and r is
// right index of the sub-array
// of arr to be sorted */
void mergeSort(int arr[],int l,int r){
    if(l>=r){
        return;//returns recursively
    }
    int m =l+ (r-l)/2;
    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m,r);
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

