
#!/usr/bin/python3

def exchange(a, b):
    temp = a
    a = b
    b = temp
    tuple = (a, b)
    return tuple

# 冒泡排序
def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if (arr[j] > arr[j+1]):
                (arr[j+1], arr[j]) = (arr[j], arr[j+1])
    return arr;


ret = bubble([1, 5, 8, 10, 2, 4, 3])
print(ret);
