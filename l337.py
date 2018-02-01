""" House Robber III """

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mdic = {}
        def rob(node, flag):
            if not node:
                return 0
            if (node,flag) in mdic:
                return mdic[(node,flag)]
            if flag == 0:
                money = max(rob(node.left,0)+rob(node.right,0), rob(node.left,0)+rob(node.right,1), rob(node.left,1)+rob(node.right,0), rob(node.left,1)+rob(node.right,1))
                mdic[(node,0)] = money
            else:
                money = node.val + rob(node.left,0)+rob(node.right,0)
                mdic[(node,1)] = money
            return money
        return max(rob(root,0), rob(root, 1))