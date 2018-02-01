""" Permutations """

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def perm(dic, ts):
            if not dic:
                ans.append(ts)
                return
            for i in dic:
                nts = list(ts)
                nts.append(i)
                ndic = list(dic)
                ndic.remove(i)
                perm(ndic,nts)
            return
        perm(nums, [])
        
        return ans

s = Solution()
print(s.permute([1,2,3]))
            
        