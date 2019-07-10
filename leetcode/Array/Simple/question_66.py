#!/usr/bin/python3

'''
对应链接：https://leetcode-cn.com/problems/plus-one/

66. 加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。


示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

'''

# 只需要注意：最后一个数字加1，可能会产生进位的问题

class Solution(object):
    # 方案一：傻傻的，一个个自动加：如果某个元素是9，则加1需要进位就好了
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digitsLen = len(digits);
        if digitsLen == 0:
            return digits;

        carry = 1; # 进位标识：默认加1
        for idx in range(0, digitsLen):
            reverseIdx = digitsLen - idx - 1;
            addNum = (digits[reverseIdx] + carry);
            if addNum == 10:
                digits[reverseIdx] = 0;
                carry = 1;
            else:
                carry = 0;
                digits[reverseIdx] = addNum;
        if carry == 1:
            digits.insert(0, 1);
        return digits;

    # 方案二：数组先转成对应的数字，再加1，自动计算后再转成数组
    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

    # 方案三：最后一个数字加1之后，进位=sum/10, 当前元素值=sum%10


    # 该种方案的解法，同67序号【Add Binary 二进制数相加】，如果两个字符串长度不同，在最前面补0，保证两个长度相同，然后倒序遍历对应位置元素相加
    # 进位=sum/2, 当前元素值=sum%2。该问题的解决方案同该题，只是针对2或者10而已
    def plusOne3(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digitsLen = len(digits);
        if digitsLen == 0:
            return digits;

        carry = 1;  # 进位标识：默认加1
        for idx in range(0, digitsLen):
            reverseIdx = digitsLen - idx - 1;
            sum = (digits[reverseIdx] + carry);
            digits[reverseIdx] = int(sum % 10);
            carry = sum / 10;
        if carry == 1:
            digits.insert(0, 1);
        return digits;


obj = Solution();

digits = [1,3,5,6];
digits = [9,8,9,9];
digits = [9,9,9,9];

plusOneDisgits = obj.plusOne3(digits)

print(plusOneDisgits);

