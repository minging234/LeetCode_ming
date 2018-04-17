""" Non-decreasing Array """

class Solution:
    def checkPossibility(self, A):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = None
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])


s = Solution()
print(s.checkPossibility([-1,4,2,3]))