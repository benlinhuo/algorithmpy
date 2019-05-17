
#!/usr/bin/python3

'''
欧几里得算法
获取最大公约数
'''

def getCommonDivisor(a, b):
    if b == 0:
        return a;
    remainder = a % b;
    return getCommonDivisor(b, remainder)




print(getCommonDivisor(10, 7));