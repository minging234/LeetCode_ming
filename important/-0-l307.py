""" Range Sum Query - Mutable """

class NumArray:

    dic = {}
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(len(nums)):
            self.dic[i] = nums[i]

    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.dic[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        total = 0
        for i in range(i,j+1):
            total += self.dic[i]
        return total

