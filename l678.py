""" Longest Univalue Path """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ans = 0
        def helper(node):
            global ans
            if not node:
                return 0
            length = 0
            left_len = helper(node.left)
            right_len = helper(node.right)

            if node.left:
                if node.left.val == node.val:
                    left_len += 1
                    length = left_len
            if node.right:
                if node.right.val == node.val:
                    right_len += 1
                    length = max(right_len, length)
            
            if node.left and node.right:
                if node.left.val == node.val and node.right.val == node.val:
                    self.ans = max(self.ans, left_len + right_len)
            self.ans = max(self.ans, length)
            return length
        
        helper(root)
        return self.ans
            


        