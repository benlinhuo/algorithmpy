
#!/usr/bin/python3

'''
对应链接：https://leetcode-cn.com/problems/two-sum/

1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''


class TwoSum:

    # 暴力解法:且结果答案可能是多种。但是它的时间复杂度是O(n^2)。效率低下
    def forceResolve(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retArr = [];
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    retArr.append([i, j]);

        return retArr;


    # 利用key-value的hashMap，空间换取时间。因为hashMap的查找效率是常数级
    # 第一步，先把原数组变成hash存储，第二步直接通过hash查找对应数据比对
    def hashMapResolve(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retArr = [];
        hashMap = {};
        for i in range(0, len(nums)):
            hashMap[nums[i]] = i;
        for i in range(0, len(nums)):
            other = target - nums[i];

            # other!=i是因为类似于4=2+2，2不能是同一个元素，如题目要求中所指"你不能重复利用这个数组中同样的元素。"
            if other in hashMap.keys() and hashMap[other] > i:
                retArr.append([i, hashMap[other]])

        return retArr;



    # 在 hashMapResolve 的基础上把2个for循环变成1个
    # 在我们比对的过程中，把遍历过的数据存放到hash map中，因为 a[1]+a[2]=target,则a[2]+a[1]=target。所以我们可以在遍历i=1时，不知道另一个时j=2，但是当i=2时，因为hash map中已经有下标为1的值，则可得出j=1
    def hashMapHigherResolve(self, nums, target):
        retArr = [];
        hashMap = {};
        for idx, num in enumerate(nums):
            other = target - num;
            if other in hashMap.keys():
                retArr.append([other, idx]); # idx 一定是大于 other
            hashMap[num] = idx;

        return retArr;


# 执行
obj = TwoSum()
targetArr = [2, 7, 11, 15, 3]
targetValue = 18

retArr = obj.forceResolve(targetArr, targetValue);
print(retArr);

retArrHash = obj.hashMapResolve(targetArr, targetValue);
print(retArrHash);

retArrHigher = obj.hashMapResolve(targetArr, targetValue);
print(retArrHigher);
