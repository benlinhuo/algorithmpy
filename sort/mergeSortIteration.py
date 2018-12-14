#!/user/bin/python3

'''
归并排序：

归并排序我们采用递归去实现（也可采用迭代的方式去实现）
一般都是将2个已有序的子序列，合并成一个大的有序序列

https://www.cnblogs.com/chengxiao/p/6194356.html

https://www.cnblogs.com/skywang12345/p/3602369.html

'''

import math;

# 将2个已有序的子序列，合并成一个大的有序序列。
# [leftStartIndex, leftEndIndex] 不包括leftEndIndex 与 [leftEndIndex, rightEndIndex] 不包括 rightEndIndex
def mergeTwoOrderedArr(arr, leftStartIndex, leftEndIndex, rightEndIndex):
    temp = [];
    i = leftStartIndex;
    j = leftEndIndex;


    # 两个独立数组，各自有对应游标，进行比较。则把2个比较条件用and作为总的比较条件
    while i < leftEndIndex and j < rightEndIndex:
        if arr[i] >= arr[j]:
            temp.append(arr[j])
            j += 1;
        else:
            temp.append(arr[i]);
            i += 1;
    # 游标j到达末尾
    for ii in range(i, leftEndIndex):
        temp.append(arr[ii]);
    # 游标i到达末尾
    for jj in range(j, rightEndIndex):
        temp.append(arr[jj]);

    for idx in range(0, len(temp)):
        arr[leftStartIndex + idx] = temp[idx];

    return arr;


# https://blog.csdn.net/jacketinsysu/article/details/52472364
# 迭代写法
def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr;
    # 步长是：1，2，4，8...
    step = 1;
    while step < (len(arr) + 1):
        offset = step * 2;
        for i in range(0, len(arr), offset):
            arr = mergeTwoOrderedArr(arr, i, min(i + step, len(arr)), min(i + offset, len(arr)))
        step = offset;
    return arr;




arr2 = [110,100,90,40,80,20,60,10,30,50,70];
retSort2 = mergeSort(arr2);
print(retSort2)

# 多类进行测试
arr = [8, 1, 5, 10, 2, 4, 8, 0];
arr = [8, 1, 5, 10, 2, 4, 9];
arr = [8, 1, 5, 10, 2, 4];
arr = [8, 1, 5, 10, 2];
arr = [8, 1, 5, 10];
retSort = mergeSort(arr);
print(retSort)

arr1 = [6, 5, 3, 1, 8, 7, 2, 4];
retSort1 = mergeSort(arr1);
print(retSort1)

