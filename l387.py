"""First Unique Character in a String"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        dic = {}
        while i < len(s):        
            if s[(i+1)::].find(s[i]) == -1:
                if not dic.has_key(s[i]):
                    return i
            dic[s[i]] = i
            i += 1
        return -1

# 这种方法很差，运行时间很长 打败了 0.92% 的人

"""
        讨论区的一种3行的方法：

        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

"""