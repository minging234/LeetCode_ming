""" Move Zeroes """

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pa = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pa += 1
                continue
            if pa == 0:
                continue
            nums[i],nums[i-pa] = nums[i-pa],nums[i]

        return  