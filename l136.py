""" Single Number """

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ddic = {}
        for i in nums:
            if i not in ddic:
                ddic[i] = 1
            else:
                ddic.pop(i, None)
        for i in ddic.items():
            return i[0]

s = Solution()
print(s.singleNumber([1,3,1,-1,3]))


"""
    这道题有一个使用XOR的 很牛逼的方法
        a = 0
        for i in nums:
            a ^= i
        return a
"""