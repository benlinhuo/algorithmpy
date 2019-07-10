#!/usr/bin/python3

'''
对应链接：https://leetcode-cn.com/problems/merge-sorted-array/

88. 合并两个有序数组

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]


'''

# 原理：因为二者都是有序的，且插入到nums1数组，所以选择从最后开始比较插入，否则还需要移动已有元素位置。（如果是从前往后的话）
# 维持3个指针，分别指向nums1最后一个元素，num2最后一个元素，以及添加完整后的num1最后一个元素。每操作一个，3个指针正确移动即可。
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1Point = m - 1;
        nums2Point = n - 1;
        fullPoint = m + n - 1;
        while nums1Point >= 0 and nums2Point >= 0:
            num1 = nums1[nums1Point];
            num2 = nums2[nums2Point];
            if num1 < num2 :
                nums1[fullPoint] = num2;
                fullPoint -= 1;
                nums2Point -= 1;
            else:
                nums1[fullPoint] = num1;
                fullPoint -= 1;
                nums1Point -= 1;
        while nums2Point >= 0:
            nums1[fullPoint] = nums2[nums2Point];
            fullPoint -= 1;
            nums2Point -= 1;
        return nums1;


obj = Solution();

nums1 = [2,3,4,0,0,0]
nums2 = [2,5,6]

mergeArr = obj.merge(nums1, 3, nums2, 3);

print(mergeArr);

