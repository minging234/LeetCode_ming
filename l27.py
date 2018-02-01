""" Remove Element """

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in nums:
            if i != val: 
                nums[count] = i
                count += 1
               
        return count
