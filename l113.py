""" Path Sum II """

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        def pathes(node, total, path):
            if not node:
                return
            path.append(node)
            total += node.val
            if node.left:
                pathes(node.left, total, path)
            if node.right:
                pathes(node.right, total, path)
            if not node.left and not node.right and total == sum:
                tmp =[]
                for i in path:
                    tmp.append(i.val)
                ans.append(tmp)
            path.pop()
            return

        pathes(root, 0, [])
        return ans

"""
这种题还有迭代的解法

        if not root:
            return []
        path = []
        stack = [(root, sum, [])]
        while stack:
            node, target, pa = stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                if node.val == target:
                    pa += [node.val]
                    path.append(pa)
                continue
            if node.left:
                stack.append((node.left, target - node.val, pa + [node.val]))
            if node.right:
                stack.append((node.right, target - node.val, pa + [node.val]))
        return path
"""


            
            

                    


