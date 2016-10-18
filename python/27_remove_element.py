#! usr/bin/python
# coding=utf-8 //这句是使用utf8编码方式方法,可以单独加入python头使用

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[j] = nums[i]
            j += 1
        if j == 0:
            nums = []
        else:
            nums = nums[0:j]
        return len(nums)


if __name__ == '__main__':
    Solution().removeElement([2,3,3,2], 3);
