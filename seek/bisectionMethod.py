
#!/usr/bin/python3

'''
二分法查找：
二分法查找，只适合于已排序的队列，如果是混乱队列，则选择其他算法
首先以队列最左和最右为边界，然后获取最中间的元素，与查找的元素比较。如果比中间元素小，则最右边界改为中间元素，重复上述步骤

比如：

有一个数组arr，已经升序排列了，现在有个数组中元素，你要怎么通过查找知道它位于什么位置

'''

def bisectionSeek(arr, ele):
    left = 0;
    right = len(arr) - 1;
    # -1表示
    index = -1;
    while left < (right - 1):
        mid = round((left + right) / 2.0);
        if ele < arr[mid]:
            right = mid;
        elif ele > arr[mid]:
            left = mid;
        elif ele == arr[mid]:
            index = mid;
            break;
    return index;



eleIndex = bisectionSeek([1, 2, 5, 8, 10, 15, 16,19, 20], 15); #数组中偶数个元素
print(eleIndex)

eleIndex2 = bisectionSeek([1, 2, 5, 8, 10, 15, 16,19], 15); #数组中奇数个元素
print(eleIndex2)

eleIndex1 = bisectionSeek([1, 2, 5, 8, 10, 15, 16,19, 20], 3);
print(eleIndex1)