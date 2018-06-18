import java.util.LinkedList;
import java.util.Stack;

// Flatten Binary Tree to Linked List

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
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void flatten(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();

        stack.push(root);
        TreeNode pre = new TreeNode(0);

        while(!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            if (curr == null) {
                continue;
            }
            pre.right = curr;
            stack.push(curr.right);
            stack.push(curr.left);
            curr.left = null;
            pre = curr;
        }
        return;
    }
}