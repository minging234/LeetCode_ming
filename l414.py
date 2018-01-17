"""Third Maximum Number"""

"""
我看错题了，写了一个返回第三个频率最高的数的程序

class Solution(object):
    def thirdMax(self, nums):
        \"""
        :type nums: List[int]
        :rtype: int
        \"""
        frq = {}
        
        for i in nums:
            if i in frq:
                frq[i] += 1
            else:
                frq[i] = 1
        
        orderd = sorted(frq.items(), key= lambda a: a[1],reverse=True)
        if len(orderd) < 3:
            return orderd[0][0]
        else:
            return orderd[2][0]

            
a = Solution()
b = a.thirdMax([1,1,1,2,2,3])
print(b)

"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        orderd = sorted(set(nums))
        if len(orderd) < 3:
            return orderd[-1]
        else:
            return orderd[-3] 


            
