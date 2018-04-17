# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None,None]

        curr = root

        dummy1 = TreeNode(-1)
        dummy2 = TreeNode(-1)

        while curr:
            if curr.val > V:
                curr = curr.left
        
        