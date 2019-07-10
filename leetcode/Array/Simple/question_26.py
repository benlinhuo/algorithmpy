#!/usr/bin/python3

'''
对应链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

26. 删除排序数组中的重复项

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。


示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

'''


'''
该问题需要注意的点是：
    1. 这是个排序点数组，也就是说同样的数字一定都在一起，不会间隔出现；
    2. 要求：不要使用额外的数组空间，在使用 O(1) 额外空间的条件下完成；
    3. 需要返回移除后数组的新长度，且数组变成新的不重复数组
    4. 你不需要考虑数组中超出新长度后面的元素。也就是我们是需要利用老数组更改元素来达到目的
'''


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newIdx = 0
        length = len(nums)
        for idx in range(0, length):
            if idx >= 1 and nums[newIdx] != nums[idx]:
                newIdx += 1;
                nums[newIdx] = nums[idx];

        return (newIdx + 1);



obj = Solution();

# targetArr = [0,0,1,1,1,2,2,3,3,4];
targetArr = [1, 1, 2, 3, 4, 4, 5, 6, 6];

retLength = obj.removeDuplicates(targetArr);

print(retLength);
print(targetArr);