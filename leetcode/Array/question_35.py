#!/usr/bin/python3

'''
对应链接：https://leetcode-cn.com/problems/search-insert-position/

35. 搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

'''

# 这道题目超级简单，就简单写写把
# 它是有序数组，所以只要找到比target数值大的就返回，判断该index对应的数字和target是否相等即可知道返回的是目标值索引，还是target应该插入的位置

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx, num in enumerate(nums):
            if num >= target:
                return idx;
        return len(nums);


obj = Solution();

targetArr = [1,3,5,6];
targetVal = 0;

insertIdx = obj.searchInsert(targetArr, targetVal)

print(insertIdx);

