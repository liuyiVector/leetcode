#! usr/bin/python
# coding=utf-8 //这句是使用utf8编码方式方法,可以单独加入python头使用
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == None or len(nums) == 0:
            return 0 
        i = 0
        j = 0
        for i in range(1,len(nums)):
            if nums[j] == nums[i]:
                continue
            j += 1
            nums[j] = nums[i]
        return j + 1

if __name__ == '__main__':
    print Solution().removeDuplicates([2,2,3])
