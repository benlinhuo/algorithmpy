#!/user/bin/python3

'''
归并排序：

归并排序我们采用递归去实现（也可采用迭代的方式去实现）
一般都是将2个已有序的子序列，合并成一个大的有序序列

https://www.cnblogs.com/chengxiao/p/6194356.html

https://www.cnblogs.com/skywang12345/p/3602369.html

'''

import math;

# 将2个已有序的子序列，合并成一个大的有序序列。需要利用一个和合并后一样大小空间的temp
# leftArr 和 rightArr 必须是有序的才可以
def mergeTwoOrderedArr(leftArr, rightArr):
    temp = [];
    i = 0;
    j = 0;

    # 两个独立数组，各自有对应游标，进行比较。则把2个比较条件用and作为总的比较条件
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] >= rightArr[j]:
            temp.append(rightArr[j])
            j += 1;
        else:
            temp.append(leftArr[i]);
            i += 1;
    # 游标j到达末尾
    for ii in range(i, len(leftArr)):
        temp.append(leftArr[ii]);
    # 游标i到达末尾
    for jj in range(j, len(rightArr)):
        temp.append(rightArr[jj]);

    return temp;


# https://blog.csdn.net/jacketinsysu/article/details/52472364
# 迭代写法
def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr;
    # 步长是：2，4，8...
    # 构造步长
    steps = [];
    step = 2;
    while step < len(arr):
        steps.append(step);
        step *= 2;
    for i in range(0, len(steps)):
        s = steps[i];
        for j in range(0, math.ceil(len(arr)))




arr2 = [110,100,90,40,80,20,60,10,30,50,70];
retSort2 = mergeSort(arr2);
print(retSort2)

arr = [1, 5, 8, 10, 2, 4, 8, 0];
# arr = [1, 5, 8, 10, 2];
retSort = mergeSort(arr);
print(retSort)

arr1 = [6, 5, 3, 1, 8, 7, 2, 4];
retSort1 = mergeSort(arr1);
print(retSort1)

