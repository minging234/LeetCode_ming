""" Generate Parentheses """

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans =[]
        def cons(s,left,right):
            if len(s) == 2*n:
                ans.append(s)
                return
            if left < n:
                cons(s+"(",left+1,right)
            if right < left:
                cons(s+")",left,right+1)
        cons("",0,0)
        return ans
            
s = Solution()
print(s.generateParenthesis(3))

""" 
    对于dfs 还需要更深入的理解

""""