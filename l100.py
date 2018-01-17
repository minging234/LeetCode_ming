""" Same Tree """

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        import collections
        stack = collections.deque()
        stack.append((p,q))

        while stack:
            node1, node2 = stack.popleft()
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            if not node1 and not node2:
                continue
            if node1.val != node2.val:
                return False
            stack.append((node1.left,node2.left))
            stack.append((node1.right,node2.right))
        
        return True