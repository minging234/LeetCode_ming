import java.awt.List;
import java.util.LinkedList;
import java.util.Stack;

// Closest Binary Search Tree Value II

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
     * @param k: the given k
     * @return: k values in the BST that are closest to the target
     */
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        if (root == null) {
            return null;
        }

        LinkedList<Integer> ans = new LinkedList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;

        while (!stack.isEmpty() || curr != null) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            if (ans.size() < k) {
                ans.offer(curr.val);
            } else if (curr.val <= target || curr.val - target < Math.abs(ans.peek() - target)) {
                ans.poll();
                ans.offer(curr.val);
            } else {
                return ans;
            }
            curr = curr.right;
        }

        return ans;
    }
}