#!/usr/bin/python3

'''
希尔排序：
本质还是插入排序，只是把它根据步长拆分成不同的段

http://www.cnblogs.com/chengxiao/p/6104371.html

'''

import math;

# 最纯粹的插入算法
def insertionSort(arr):
    for i in range(1, len(arr)):
        currEle = arr[i]
        for j in range(i - 1, -1, -1):
            if currEle < arr[j]:
                (arr[j+1], arr[j]) = (arr[j], arr[j+1])
                # (arr[i], arr[j]) = (arr[j], arr[i])  不能用arr[i]和arr[j]交换，是因为在交换过一次之后，arr[i]的值就已经发生变化了
            else:
                break;

    return arr;

def shellSort(arr):
    stepSize = [5, 2, 1]; # 越往后越有序，所以步长越小
    for step in stepSize:
        for i in range(0, step):
            newshortarr = []; # 空列表创建
            for k in range(0, math.floor((len(arr) - 1) / step) + 1):
                newshortarr.append(arr[step * k + i]);
            newshortarr = insertionSort(newshortarr); # 有序

            for kk in range(0, math.floor((len(arr) - 1) / step) + 1):
                arr[step * kk + i] = newshortarr[kk];

    return arr;




retSort2 = shellSort([2, 1, 5, 10, 8]);
print(retSort2)

# retSort = shellSort([1, 5, 8, 10, 2, 4, 8, 0]);
# print(retSort)
#
# retSort1 = shellSort([6, 5, 3, 1, 8, 7, 2, 4]);
# print(retSort1)
