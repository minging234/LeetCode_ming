"""Construct the Rectangle"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = 1
        l = area
        ans = [l,w]
        while w <= area :
            w += 1
            if area % w == 0:
                l = area / w
                if l >= w:
                    ans = [l,w]
                else:
                    return ans
        return ans

# 打败了 7.7% 的人

""" 
    以下是有人给出的使用math的方法
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1
"""