""" Combination Sum """

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort(reverse=True)
        def dfs(ind, li, target):
            if target == 0:
                ans.append(li)
                return
            if ind == len(candidates):
                return   
            while target >= 0:
                nex = list(li)
                dfs(ind+1,nex,target)
                li.append(candidates[ind])
                target -= candidates[ind]
            return
        dfs(0,[],target)
        return ans

s = Solution()
print(s.combinationSum([2,3,6,7],7))

"""

        candidates = sorted(candidates)
        sols = []

        def cshelp(last, cur, target):
            if target == 0:
                sols.append(cur)
            elif target < candidates[0]:
                return
            else:
                for i, cand in enumerate(candidates):
                    if i >= last:
                        cshelp(i, cur+[cand], target-cand)
                       
        cshelp(0, [], target)
        
        return sols

"""