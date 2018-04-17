""" Unique Binary Search Trees II """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def search(l,r):
            a = []
            if l >= r:
                a.append(None)
                return a

            for i in range(l,r):
                left = search(l,i)
                right = search(i+1,r)

                for lnode in left:
                    for rnode in right:
                        root = TreeNode(i)
                        root.left = lnode
                        root.right = rnode
                        a.append(root)
            return a
        
        if n == 0:
           return [] 
        return search(1,n+1)


s = Solution()
print(s.generateTrees(0))
        
                
                



        