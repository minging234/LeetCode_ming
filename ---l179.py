""" Largest Number """

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num




"""
    以下是我的错误答案，对于将什么数字放在前面没有准确的理解
        ans = ''
        def comp(num1, num2):
            n1, n2 = num1, num2
            d1 = d2 = 1
            while n1 >10:
                n1 = int(n1/10)
                d1 += 1
            while n2 >10:
                n2 = int(n2/10)
                d2 += 1
            c1 = n1%10
            c2 = n2%10
            if c1 != c2:
                return c1 > c2
            elif d1 != d2:
                return d1 < d2 
            else:
                return n1 > n2
        for i in range(1,len(nums)):
            j = i
            while j > 0:
                if comp(nums[j],nums[j-1]):
                    nums[j],nums[j-1] = nums[j-1],nums[j]
                    j -= 1
                else:
                    break
        for i in nums:
            ans += str(i)
        return ans
"""






