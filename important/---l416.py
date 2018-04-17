""" Partition Equal Subset Sum """

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)/2
        if int(target) != target:
            return False
        target = int(target)

        dp =[[False for i in range(target+1)] for i in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = True

        for j in range(1,target+1):
            dp[0][j] = False

        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = (dp[i][j] or dp[i-1][j-nums[i-1]])
        return dp[-1][-1]

s = Solution()
print(s.canPartition([1,2,5]))

"""
    以上是使用dp的解法，但是在 python 中是超时的
    
    另一种是直接更新一个字典，算出所有可能的情况，是O(n^2)的方法，可以通过

        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (sum(nums) / 2.)  in possible_sums 

    最快的方式是使用dfs 加上剪枝

                # get sum
        val_sum = sum(nums)
        
        if val_sum % 2 == 1:
            # odd sum
            return False
        
        val_half = val_sum//2
        
        # Search for a sum of val_half
        #   Similar to Combinatorial Sum
        
        # sort it (reverse)
        nums.sort(reverse = True)
    
        # DFS
        def dfs(i, target):
            # in nums[i:] look for subset of sum of target
            if target == 0:
                return True
            if i == len(nums) or target < 0:
                return False
            
            # prune
            if nums[i] > target:
                return False
            
            # i < len(nums), target > 0
            return dfs(i+1, target - nums[i]) or dfs(i+1, target)
        
        return dfs(0, val_half)

