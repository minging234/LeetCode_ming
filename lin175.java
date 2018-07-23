import java.util.LinkedList;

// Invert Binary Tree

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
    // public void invertBinaryTree(TreeNode root) {
    //     if (root == null) return;
    //     helper(root);
    // }

    // private TreeNode helper(TreeNode node) {
    //     if (node == null) return null;
    //     TreeNode temp = node.left;
    //     node.left = helper(node.right);
    //     node.right = helper(temp);
    // }

    public void invertBinaryTree(TreeNode root) {
        if (root == null) return;
        LinkedList<TreeNode> list = new LinkedList<>();
        list.offerLast(root);
        TreeNode node;
        TreeNode temp;

        while (!list.isEmpty()) {
            node = list.pollFirst();
            if (node == null) continue;
            temp = node.left;
            node.left = node.right;
            node.right = temp;
            list.offerLast(node.left);
            list.offerLast(node.right);
        }
        return;
    }
}