// Minimum Subtree

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: the root of the minimum subtree
     */
    public TreeNode findSubtree(TreeNode root) {
        // write your code here
        if (root == null) {
            return root;
        }
        helper(root);
        return this.ans;
    }

    private int minval = Integer.MAX_VALUE;
    private TreeNode ans = null;

    private int helper(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int nodeVal = node.val + helper(node.left) + helper(node.right);

        if (nodeVal < this.minval) {
            this.ans = node;
            this.minval = nodeVal;
        }
        return nodeVal;
    }
}