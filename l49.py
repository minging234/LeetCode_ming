""" Group Anagrams """

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        dic = {}
        for i in strs:
            p = tuple(sorted(i))
            if p in dic:
                ans[dic[p]].append(i)
            else:
                ans.append([i])
                dic[p] = len(ans)-1
        return ans

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))