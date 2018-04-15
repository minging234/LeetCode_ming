class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        maxarea = 0
        for i in range(len(points)):
            # print(points[i][0])
            for j in range(i,len(points)):
                for k in range(j,len(points)):                    
                    S = 0.5 *abs(points[i][0]*points[j][1] + points[j][0]*points[k][1] + points[k][0]*points[i][1] - points[i][0]*points[k][1] - points[j][0]*points[i][1] - points[k][0]*points[j][1])
                    maxarea = max(maxarea, S)

        return maxarea
    
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def helper(node):
            if node is None:
                return True
            if node.val == 1:
                flag = False
            else:
                flag = (helper(node.left) and helper(node.right))
            
            if helper(node.left):
                node.left = None
            if helper(node.right):
                node.right = None
            return flag

        helper(root)
        return root

    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        ans = []
        a = sorted(A)
        for i in range(K-1):
            ans.append([a[len(a)-i-1]])
        ans.append(a[:len(a)-K+1])
        print(ans)
        result = 0
        for li in ans:
            result += sum(li)/len(li)

        return result
        












So = Solution()
# print (So.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]) )   
print(So.largestSumOfAverages([4,1,7,5,6,2,3],4))