
#!/usr/bin/python3


def bisectionInsertionSort(arr):
    if len(arr) == 0:
        return arr;
    # 特别要注意的是：range方法 range(a, b, interval)  不包含b
    for i in range(1, len(arr)):
        ele = arr[i];
        left = 0;
        right = i - 1;
        # 根据中间标签移动，最后必须要left和right合二为一便是该元素应该对应的位置
        while left <= right:
            mid = round((left + right) / 2);
            if ele < arr[mid]:
                right = mid - 1;
            else:
                left = mid + 1;
        # 元素移动：把要插入的index之后的元素都往后移动腾出位置 （只能用left,因为right某些情况会变成-1）
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j];
        arr[left] = ele;
    return arr;




retSort2 = bisectionInsertionSort([2, 1, 5, 10, 8]);
print(retSort2)

retSort = bisectionInsertionSort([1, 5, 8, 10, 2, 4, 8, 0]);
print(retSort)

retSort1 = bisectionInsertionSort([6, 5, 3, 1, 8, 7, 2, 4]);
print(retSort1)