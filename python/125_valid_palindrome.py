#! usr/bin/python
# coding=utf-8 //这句是使用utf8编码方式方法,可以单独加入python头使用

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (not s) or (not s.strip()):
            return True
        else:
            tmp = []
            for item in s:
                if item.isalpha() or item.isdigit():
                    tmp.append(item)
            size = len(tmp)
            for i in range(0, size/2):
                if tmp[i].upper() != tmp[size - 1 - i].upper():
                    return False
            return True


if __name__ == "__main__":
    print Solution().isPalindrome('A man, a plan, a canal: Panama')
