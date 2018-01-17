""" Top K Frequent Elements"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        dic = {}
        frq = []
        ans = []

        for i in nums:
            if dic.has_key(i):
                dic[i] +=1
            else:
                dic[i] = 1
        
        for i in dic.items():
           heapq.heappush(frq,(-i[1],i[0]))
        
        n = 1
        while n <= k:
            ans.append(heapq.heappop(frq)[1])
            n += 1

        return ans