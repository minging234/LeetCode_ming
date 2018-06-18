// Lowest Common Ancestor

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
    /*
     * @param root: The root of the binary tree.
     * @param A: A TreeNode
     * @param B: A TreeNode
     * @return: Return the LCA of the two nodes.
     */
    public TreeNode lowestCommonAncestor3(TreeNode root, TreeNode A, TreeNode B) {
        helper(root, A, B);
        return this.ans;
    }

    private TreeNode ans = null;

    private int helper(TreeNode node, TreeNode A, TreeNode B) {
        if (node == null) {
            return 0;
        }
        int count = 0;

        if (node == A) {
            count ++;
        }
        if (node == B) {
            count ++;
        }
        
        count += helper(node.left, A, B) + helper(node.right, A, B);

        if (count == 2 || this.ans != null) {
            this.ans = node;
        }

        return count;
    }
}