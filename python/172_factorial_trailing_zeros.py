#! usr/bin/python
# coding=utf-8 //这句是使用utf8编码方式方法,可以单独加入python头使用


#阶乘结果尾数0的个数和5的因素个数一致，因为2总比5多，只考虑5

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        result = 0
        while n / 5 > 0:
            n = n / 5
            result += n
        return result



if __name__ == '__main__':
    print Solution().trailingZeroes(30)
