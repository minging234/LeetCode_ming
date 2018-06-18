import java.util.Stack;

// Kth Smallest Element in a BST

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
     * @param k: the given k
     * @return: the kth smallest element in BST
     */
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();

        // stack.add(root);
        TreeNode curr = root;
        int count = 1;

        while (!stack.isEmpty() || curr != null) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            if (count == k) {
                return curr.val;
            }
            curr = curr.right;
            count ++;
        }

        return -1;
    }
}