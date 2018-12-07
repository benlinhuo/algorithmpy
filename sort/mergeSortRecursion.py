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


# 递归写法：分而治之（先逐步拆分至单个元素，再两两合并排序）
def mergeSortWithRecursion(arr, left, right):
    if left >= right:
        return [arr[left]];
    mid = math.floor((left + right) / 2); # 易错点：容易把 math.floor 错写成 round，应该是向下取整，否则造成死循环
    # 先拆分
    leftArr = mergeSortWithRecursion(arr, left, mid);
    rightArr = mergeSortWithRecursion(arr, mid + 1, right);
    # 后合并排序
    arr = mergeTwoOrderedArr(leftArr, rightArr);
    return arr;

def mergeSort(arr):
    return mergeSortWithRecursion(arr, 0, len(arr) - 1);


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

