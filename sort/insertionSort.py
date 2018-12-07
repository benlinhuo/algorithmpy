
#!/usr/bin/python3

'''
插入排序：
具体算法描述如下：
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5

'''

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




retSort2 = insertionSort([1, 2, 5, 10, 8]);
print(retSort2)

retSort = insertionSort([1, 5, 8, 10, 2, 4, 8, 0]);
print(retSort)

retSort1 = insertionSort([6, 5, 3, 1, 8, 7, 2, 4]);
print(retSort1)
