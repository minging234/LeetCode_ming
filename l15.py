nums = [1,2,3,-1,-2,-3,0]


def threeSum(nums):
    listm = {}
    ans = []
    for i in range(len(nums)):
        listm[nums[i]] = i

    for i in range(len(nums)):
        tar = 0 - nums[i]
        for j in range(i+1,len(nums)):
            if tar - nums[j] in listm:
                if nums[i] <= nums[j] <= tar - nums[j]:
                    ans.append([nums[i],nums[j],tar-nums[j]])

    return ans




print(threeSum(nums))


def threeSum(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
