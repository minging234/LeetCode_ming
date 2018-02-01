""" Binary Tree Level Order Traversal """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def helper(node, layer):
            if not node:
                return
            if len(ans) < layer:
                ans.append([node.val])
            else:
                ans[layer-1].append(node.val)
            helper(node.left, layer+1)
            helper(node.right, layer+1)
            return
        helper(root,1)
        return ans

