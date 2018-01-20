""" Largest Rectangle in Histogram """

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
        
       


""" 
    想出了一个简介的 O(n^2) 的方法，可惜会超时
    if not heights:return 0
        cut = min(heights)
        area = cut * len(heights)
        pos = heights.index(cut)
        return max(area, self.largestRectangleArea(heights[:pos]), self.largestRectangleArea(heights[pos+1:]))，

    答案中，有个解法，利用一个栈来进行记录操作，在数组的最后加上一个假的值 “0”，并在栈中加入“-1”来指向这个伪值。 
    即可以防止数组越界，又可以使得所有元素都被扫描到。算法过程中，每一个 计算i 的过程，实际上都是对i以前的元素的运算

    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
"""
