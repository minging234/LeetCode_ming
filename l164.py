



def maximumGap(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)<2:
        return 0
    nums.sort()
    a = nums[0]
    maxg = 0
    for i in nums:
        if i - a >maxg:
            maxg = i - a
        a = i

    return maxg





a = [1,2,3,4,5,32,1,2,3,4]

print(maximumGap(a))
