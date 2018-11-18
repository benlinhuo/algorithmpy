
#!/usr/bin/python3

'''
选择排序
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置；然后，再从剩余未排序元素中继续寻找最小（大）元素，放到已排序序列的末尾。
'''

def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = arr[i];
        k = i;
        for j in range(i, len(arr)):
            if min > arr[j]:
                min = arr[j];
                k = j;
        (arr[i], arr[k]) = (arr[k], arr[i]);

    return arr;



# 即使是空数据，for 循环也没问题
retSort2 = selectionSort([]);
print(retSort2)



retSort = selectionSort([1, 5, 8, 10, 2, 4, 8, 0]);
print(retSort)

retSort1 = selectionSort([6, 5, 3, 1, 8, 7, 2, 4]);
print(retSort1)