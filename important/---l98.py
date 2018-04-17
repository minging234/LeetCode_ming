"""Validate Binary Search Tree"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre = None
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            top = stack.pop()
            if pre is not None and pre.val >= top.val:
                return False
            pre = top
            curr = top.right
        return True

a = TreeNode(1)
b = TreeNode(0)
c = TreeNode(2)
a.left = b
a.right = c
s = Solution()
print(s.isValidBST(a))

