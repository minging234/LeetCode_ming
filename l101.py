""" Symmetric Tree """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def search(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False 
            if node1.val != node2.val:
                return False
            return search(node1.left, node2.right) and search(node1.right, node2.left)
        if not root:
            return True
        return search(root.left,root.right)
        