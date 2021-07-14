# Algorithm
## Sorting
- 排序算法的稳定性：稳定排序算法会让原本有相等键值的记录维持相对次序
- 数据交换trick: 利用索引进行交换
```bash
[i], [i+1] = [i+1], [i]
```
**注意**：i，j 不仅代表内外循环次数，且在表示a_list元素索引
###Bubble Sort（冒泡排序）

- 时间复杂度\
O(n<sup>2</sup>)\
  最优情况时间复杂度为O(n)。(列表原顺序即为最终顺序，此时仅执行一次for循环)
- 稳定性\
稳定，冒泡排序不改变相等值的原排列顺序
```python
def bubble_sort(a_list):
    for i in range(len(a_list) - 1):
        stop = False
        while not stop:
            for j in range(len(a_list) - 1 - i):
                stop = True
                if a_list[j + 1] < a_list[j]:
                    a_list[j], a_list[j + 1] = a_list[j+ 1], a_list[j]  # trick:利用下标对元素进行交换
                    stop = False
```
### Select Sort（选择排序）
前一部分为有序数列，后一部分为无序数列，从后部依次找到最小后放入前部，直到结束
- 时间复杂度\
O(n<sup>2</sup>)
- 稳定性\
不稳定（考虑按降序排列，即每次交换选择最大值的情况）
```python
def select_sort(a_list):
    for i in range(len(a_list)-1):
        min_index = i
        for j in range(i+1, len(a_list)):
            if a_list[min_index] > a_list[j]:
                min_index = j                          # 找到最小值对应的index
        a_list[min_index], a_list[i] = a_list[i], a_list[min_index]  
```
### Insertion Sort（插入排序）
通过构建有序序列，对于为排序序列，在已排序序列中从后往前扫描，找到相应位置并插上。
- 插入排序trick：内循环从后向前进行比较，即按`负索引`:`range(i, 0, -1)`\
  在内循环内执行的类似与**局部冒泡排序**
- 时间复杂度\
O(n<sup>2</sup>)\
最优情况时间复杂度：O(n)(升序排列)  
- 稳定性\
稳定
 ```python
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        for j in range(i, 0, -1):            # 类局部冒泡
            if a_list[j] < a_list[j-1]:
                a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
``` 
### Shell Sort（希尔排序）
希尔排序是插入排序的一种，是其更高效的改进版。希尔排序是将数组列在一个表中并对列分别进行插入排序，重复这个过程，不过每次用更长的列（步长更长了，列数更少了）来进行。
```python
def shell_sort(a_list):
    gap = len(a_list) // 2
    while gap > 0:
        for i in range(gap, len(a_list)):
            # i = [gap, gap+1, ... n-1]
            for j in range(i, 0, -gap):
                # j = [i, i-gap]
                if a_list[j] < a_list[j-gap]:
                    a_list[j], a_list[j-gap] = a_list[j-gap], a_list[j]
        gap = gap // 2
```

### Quick Sort（快速排序）
整个数组找基准值的正确位置，比基准值小的所有元素都放在基准值的前面，比基准值大的所有元素均放在基准值的后面，之后继续对左右两部分递归处理

```python
def quick_sort(a_list, left=0, right=None):
    if right == None:
        right = len(a_list)-1
    low = left
    high = right
    if left >= right:       # 递归的退出条件
        return
    temp = a_list[left]
    while low != high:
        while a_list[high] >= temp and low < high:
            high -= 1
        while a_list[low] <= temp and low < high:
            low += 1
        a_list[high], a_list[low] = a_list[low], a_list[high]

    a_list[left], a_list[low] = a_list[low], temp
    # 剩余进行递归
    quick_sort(left, low-1)
    quick_sort(low+1,right)
```

### Merge Sort（归并排序）
先递归分解数组，再合并数组
```python
def merge_sort(a_list):
    n = len(a_list)
    if n <= 1:
        return a_list
    mid = n // 2
    left_list = merge_sort(a_list[:mid])
    right_list = merge_sort(a_list[mid:])

    left_pointer, right_pointer = 0, 0
    sort_list = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            sort_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            sort_list.append(right_list[right_pointer])
            right_pointer += 1
    sort_list += left_list[left_pointer:]
    sort_list += right_list[right_pointer:]

    return sort_list
```

### 常见排序算法效率比较
| Sorting Algorithm     | 平均情况 | 最好情况 | 最坏情况 | 辅助空间 | 稳定性 |
| --------------- | --------------------- | ---------------- | ---------------- | ------ | ------- |
| Bubble Sort    |  O(n<sup>2</sup>)          | O(n)              | O(n<sup>2</sup>)  | O(1) | 稳定  |
| Select Sort    | O(n<sup>2</sup>)           | O(n<sup>2</sup>)  | O(n<sup>2</sup>)  | O(1) | 不稳定  | 
| Insertion Sort | O(n<sup>2</sup>            | O(n)              | O(n<sup>2</sup>)  | O(1) | 稳定  |
| Shell Sort     | O(nlogn)~O(n<sup>2</sup>)  | O(n<sup>1.3</sup>)| O(nlogn)          | O(1) | 不稳定 | 
| Quick Sort     | O(nlogn)                   | O(nlogn)          | O(nlogn)          | O(1) | 稳定  | 
| Merge Sort     | O(nlogn)                   | O(nlogn)          | O(n<sup>2</sup>)  | O(1) | 不稳定  |

## Search

## DP
