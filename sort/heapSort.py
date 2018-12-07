#!/usr/bin/python3

'''
堆排序：

最大堆进行升序排序的基本思想：
① 初始化堆：将数列a[1...n]构造成最大堆。
② 交换数据：将a[1]和a[n]交换，使a[n]是a[1...n]中的最大值；然后将a[1...n-1]重新调整为最大堆。
接着，将a[1]和a[n-1]交换，使a[n-1]是a[1...n-1]中的最大值；然后将a[1...n-2]重新调整为最大值。 依次类推，直到整个数列都是有序的。

"数组实现的二叉堆的性质"。
在第一个元素的索引为 0 的情形中：
性质一：索引为i的左孩子的索引是 (2*i+1);
性质二：索引为i的左孩子的索引是 (2*i+2);
性质三：索引为i的父结点的索引是 floor((i-1)/2);

最后一个非叶子节点，对应的index = 数组count / 2 - 1

https://www.cnblogs.com/skywang12345/p/3602162.html

https://www.cnblogs.com/chengxiao/p/6129630.html

'''

# 构造最大堆 ：升序；同理，最小堆针对降序
# 构造 0 ～ maxIndex 的最大堆
def structureMaximumHeap(arr, maxIndex):
    lastNotLeafIndex = round((maxIndex + 1) / 2) - 1; # 最后一个非叶子节点
    for i in range(lastNotLeafIndex, -1, -1):
        if (i * 2 + 1) <= maxIndex and arr[i * 2 + 1] > arr[i]: # 左孩子
            (arr[i * 2 + 1], arr[i]) = (arr[i], arr[i * 2 + 1])
        if (i * 2 + 2) <= maxIndex and arr[i * 2 + 2] > arr[i]: # 右孩子
            (arr[i * 2 + 2], arr[i]) = (arr[i], arr[i * 2 + 2])

    return arr;


def heapSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr;
    for i in range(len(arr) - 1, -1, -1):
        arr = structureMaximumHeap(arr, i);
        (arr[i], arr[0]) = (arr[0], arr[i])
    return arr;



# arr2 = [46, 30, 82, 90, 56, 17, 95, 15];
arr2 = [110,100,90,40,80,20,60,10,30,50,70];
retSort2 = heapSort(arr2);
print(retSort2)


arr = [1, 5, 8, 10, 2, 4, 8, 0];
retSort = heapSort(arr);
print(retSort)

arr1 = [6, 5, 3, 1, 8, 7, 2, 4];
retSort1 = heapSort(arr1);
print(retSort1)