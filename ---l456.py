""" 132 Pattern """

class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        stack = []
        m = [nums[0]]
        for i in range(1,len(nums)):
            m.append(min(m[i-1],nums[i]))

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > m[i]:
                while stack and stack[-1] <= m[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False

               

s = Solution()
print(s.find132pattern([26,2,3,4]))


""" 
    超时的方法

        if len(nums) < 3:
            return False

        lo = nums[0]
        mid = None
        ran = [[lo,mid]]

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            for r in ran:
                if r[1] is None:
                    if nums[i] < r[0]:
                        r[0] = nums[i]
                    else:
                        r[1] = nums[i]
                elif nums[i] > r[0] and nums[i] < r[1]:
                    return True
                elif nums[i] < r[0]:
                    ran.append([nums[i],None])
                else:
                    r[1] = max(r[1],nums[i]) 
        return False  
"""