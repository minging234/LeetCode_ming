""" Maximum Depth of Binary Tree """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, n):
            if not node:
                return n
            return max(dfs(node.left,n+1),dfs(node.right,n+1))

        return dfs(root,0)
