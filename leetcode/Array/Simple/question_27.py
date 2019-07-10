#!/usr/bin/python3

'''
对应链接：https://leetcode-cn.com/problems/remove-element/

27. 移除元素

给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

'''

# 该问题其实比较简单，因为我们只要用个变量记录与给定的值不同，即把正确的值（与给定的值）在遍历过程中，一个个往前移动就好了。
# 因为不需要考虑数组中超出新长度后面的元素，所以不用管和指定元素相等的放哪儿，甚至于丢弃
# 同题目26号很类似


class Solution(object):

    def removeElement(self, nums, target):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newIdx = 0;
        length = len(nums);
        for idx in range(0, length):
            if nums[idx] != target:
                nums[newIdx] = nums[idx]; # 不着急，咋们遇到一个和给定值不同的，就移过去.
                newIdx += 1;

        return (newIdx);


obj = Solution();

targetArr = [0,1,2,2,3,0,4,2]
target = 2

remainLength = obj.removeElement(targetArr, target);

print(remainLength);
print(targetArr);









