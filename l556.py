""" Next Greater Element III """

class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return -1
        nums = list(str(n))

        for i in range(len(nums)-1,-1,-1):
            m = "a"
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    if m > nums[j]:
                        m = nums[j]
            if m != "a":
                b = list(nums[i:])
                b.remove(m)
                a = nums[:i] + [m] + sorted(b)
                ans = int(''.join(a))
                if ans  > 2147483647:
                    return -1
                else:
                    return ans  
        return -1





s = Solution()
print(s.nextGreaterElement(12443322))                  

"""
    自己写的错误方法，没有考虑到所有的情况，得到的结果可能不是最小
        if n < 10:
            return -1
        num = list(str(n))
        p1 = p2 = len(num)-1
        p1 -= 1
        flag = 0

        while p1>=0 and p2 < len(num) :
            # print(flag,num[p1],num[p2])
            if flag == 0:
                if num[p1] < num[p2]:
                    # print(' --',p1,p2)
                    num[p2],num[p1] = num[p1],num[p2]
                    flag = 1
                    p1 += 1
                    p2 += 1
                    continue
                p1 -= 1
                p2 -= 1
            elif flag == 1:
                if num[p2] < num[p1] and flag == 1:
                    # print(p1,p2)
                    num[p2],num[p1] = num[p1],num[p2]
                p1 += 1
                p2 += 1
        ans = int(''.join(num))
        if flag == 0 or ans  > 2**32-1:
            return -1
        else:
            return ans

"""