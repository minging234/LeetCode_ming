""" Count Binary Substrings """

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero_stack = 0
        one_stack = 0
        ans = 0
        pre = s[0]
        for i in range(len(s)):
            if s[i] == '0':
                if pre == '1' and zero_stack != 0:
                    zero_stack = 1
                else:
                    zero_stack += 1
                if zero_stack <= one_stack:
                    ans += 1
            if s[i] == '1':
                if pre == '0' and one_stack != 0:
                    one_stack = 1
                else:
                    one_stack += 1
                if one_stack <= zero_stack:
                    ans += 1
            pre = s[i]
        return ans
            
                