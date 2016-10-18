#! usr/bin/python
# coding=utf-8 //这句是使用utf8编码方式方法,可以单独加入python头使用

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        forward = 1
        digits.reverse()
        for i in range(0,len(digits)):
            digits[i] = digits[i] + forward
            forward = digits[i]/10
            digits[i] %= 10
        if forward == 1:
            digits.append(1)
        digits.reverse()
        return digits

if __name__ == '__main__':
    print Solution().plusOne([9,9,9,9])
