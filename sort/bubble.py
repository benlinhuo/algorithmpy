
#!/usr/bin/python3

def exchange(a, b):
    temp = a
    a = b
    b = temp
    tuple = (a, b)
    return tuple

# 冒泡排序

'''
原理：
1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''

def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if (arr[j] > arr[j+1]):
                (arr[j+1], arr[j]) = (arr[j], arr[j+1])
    return arr;


ret = bubble([1, 5, 8, 10, 2, 4, 3])
print(ret);
