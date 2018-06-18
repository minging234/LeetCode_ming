import java.util.Stack;

// Validate Binary Search Tree

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
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    // public boolean isValidBST(TreeNode root) {
    //     if (root == null) {
    //         return true;
    //     }        

    //     Stack<TreeNode> stack = new Stack<>();
    //     TreeNode curr = root;
    //     TreeNode pre = null;

    //     while (!stack.isEmpty() || curr != null) {
    //         while (curr != null) {
    //             stack.push(curr);
    //             curr = curr.left;
    //         }
    //         curr = stack.pop();

    //         if (pre != null && curr.val <= pre.val){
    //             return false;
    //         }
    //         pre = curr;
    //         curr = curr.right;
    //     }
    //     return true;
    // }

    public boolean isValidBST(TreeNode root) {
        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean helper(TreeNode node, long min, long max) {
        if (node == null) return true;

        if (node.val <= min || node.val >= max) {
            return false;
        }
        return helper(node.left, min, node.val) && helper(node.right, node.val, max);
    }

}