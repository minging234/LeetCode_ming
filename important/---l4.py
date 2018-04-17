""" Median of Two Sorted Arrays """

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return None

        imin, imax, half = 0, m, int((m + n)/2)
        while imax >= imin:
            i = int((imax + imin)/2)
            j = half - i 
            if i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == m: right = nums2[j]
                elif j == n: right = nums1[i]
                else: right = min(nums1[i], nums2[j])

                if (m+n)%2 == 1:
                    return right

                if i == 0: left = nums2[j-1]
                elif j == 0: left = nums1[i-1]
                else: left = max(nums2[j-1],nums1[i-1])
                return (left + right)/2.0

s = Solution()
print(s.findMedianSortedArrays([1],[2,3,4]))
            


