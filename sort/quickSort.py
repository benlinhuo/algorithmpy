#!/usr/bin/python3

'''
步骤：
1. 先手动纸上写个列子出来，手动排序；(该例子可以尽量简单)
2. 依据写的例子开始写代码，如果不对，断点运行，就用纸上写的列子来运行有问题的地方，一眼就能看出；
3. 上述写的代码因为是流水代码，可能是比较挫，看有没需要优化的点
'''

# 获取基准值所对应的index
def getBenchmarkIndex(arr, left, right):
    key = arr[left];  # 选择最左侧为基准值
    start = left;
    end = right;
    while start < end:  # 易错之处：条件不能包括 start == end
        while start < end and key <= arr[end]:
            end -= 1;
        if start < end:
            (arr[start], arr[end]) = (arr[end], arr[start])
            start += 1;
            while start < end and key >= arr[start]:
                start += 1;
            if start < end:
                (arr[end], arr[start]) = (arr[start], arr[end])
    return start;



    return ;

# 递归：依据基准值分为左右2个部分
def quickSort(arr, left, right):
    if len(arr) == 0 or len(arr) == 1:
        return arr;
    if left < right:
        benchmarkIndex = getBenchmarkIndex(arr, left, right);
        quickSort(arr, left, benchmarkIndex - 1);
        quickSort(arr, benchmarkIndex + 1, right);
    return arr;


arr2 = [46, 30, 82, 90, 56, 17, 95, 15];
retSort2 = quickSort(arr2, 0, len(arr2) - 1);
print(retSort2)


arr = [1, 5, 8, 10, 2, 4, 8, 0];
retSort = quickSort(arr, 0, len(arr) - 1);
print(retSort)

arr1 = [6, 5, 3, 1, 8, 7, 2, 4];
retSort1 = quickSort(arr1, 0, len(arr1) - 1);
print(retSort1)



'''
快速排序：

它是对冒泡排序的改进：
快速排序的基本思想是，通过一轮的排序将序列分割成独立的两部分，其中一部分序列的关键字（这里主要用值来表示）均比另一部分关键字小。
    继续对长度较短的序列进行同样的分割，最后到达整体有序。在排序过程中，由于已经分开的两部分的元素不需要进行比较，故减少了比较次数，降低了排序时间。

下面我们通过一个案例来演示一下快速排序的基本步骤： 以序列 46 30 82 90 56 17 95 15   共8个元素

　　　　初始状态：     46  30  82  90  56  17  95  15        选择46 作为基准值，i = 0， j = 7

　　　　　　　　　　　i = 0                       j = 7

　　　　　　             15  30  82  90  56  17  95  46       15 < 46， 交换 15 和 46，移动 i， i = 1

　　　　　　　　　　　　　i = 1                       j = 7

　　　　　　　　　　  15  30  82  90  56  17  95  46       30 < 46， 不需要交换，移动 i ， i = 2

　　　　　　　　　　　　　i = 2                   j = 7

　　　　　　　　　　  15  30  46  90  56  17  95  82       82 > 46， 交换82 和 46，移动 j ， j = 6

　　　　　　　　　　　　　　　i = 2               j = 6

　　　　　　　　　　  15  30  46  90  56  17  95  82       95 > 46， 不需要交换，移动 j ， j = 5

　　　　　　　　　　　　　　　i = 2           j = 5

　　　　　　　　　　  15  30  17  90  56  46  95  82       17 < 46， 交换46 和 17，移动 i， i = 3

　　　　　　　　　　　　　　　i = 3       j = 5

　　　　　　　　　　  15  30  17  46  56  90  95  82       90 > 46， 交换90 和 46，移动 j ， j = 4

　　　　　　　　　　　　　　　    3 = i    j = 4

　　　　　　　　　　  15  30  17  46  56  90  95  82       56 > 46， 不需要交换，移动 j ， j = 3

　　　　　　　　　　　　　　　      i  =  j = 3



// 经过一轮比较之后，我们发现，关键字key已经找到了自己的位置。

当基数值不能很好地分割数组，即基准值将数组分成一个子数组中有一个记录，而另一个子组组有 n -1 个记录时，下一次的子数组只比原来数组小 1，这是快速排序的最差的情况。
如果这种情况发生在每次划分过程中，那么快速排序就退化成了冒泡排序，其时间复杂度为O(n2)。

实现方式有多种：https://blog.csdn.net/qq_36528114/article/details/78667034

https://www.cnblogs.com/surgewong/p/3381438.html

'''


