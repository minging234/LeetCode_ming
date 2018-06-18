// Closest Binary Search Tree Value

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
     * @param root: the given BST
     * @param target: the given target
     * @return: the value in the BST that is closest to the target
     */
    public int closestValue(TreeNode root, double target) {
        if (root == null) {
            return -1;
        }
        this.closest = root.val;
        helper(root, target);
        return this.closest;
    }

    private int closest;

    private void helper(TreeNode node, double target) {
        if (node == null) return;
        if (node.val == target) {
            this.closest = node.val;
            return;
        } 
        if (Math.abs(target - node.val) < Math.abs(target - closest)) {
            this.closest = node.val;
        }
        if (node.val < target) {
            helper(node.right, target);
        } else {
            helper(node.left, target);       
        }
        return;
    }
}