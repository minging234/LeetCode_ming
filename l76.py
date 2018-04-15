""" Minimum Window Substring """

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        slow = 0
        fast = 0
        ans = collections.Counter(t)
        missing = len(t)

        while fast < len(s):  
            if s[fast] in ans:
                while (s[slow] not in ans) or (s[slow] in s[slow+1:fast+1]):
                    slow += 1
                    if slow == fast:
                        break
                flag = 1
                for i in ans:
                    if i not in s[slow:fast+1]:
                        flag = 0

                if len(res) > fast - slow + 1 and flag == 1:
                    res = s[slow:fast+1]
            fast += 1

        return res if len(res) <= len(s) else ""

s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))