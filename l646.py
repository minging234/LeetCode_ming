""" Maximum Length of Pair Chain """

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        opairs = sorted(pairs)
        back = float('-inf')
        length = 0
        for i in opairs:
            if i[0] > back:
                length += 1
                back = i[1]
            elif i[1] < back:
                back = i[1]
        return length

