import java.util.LinkedList;

// Binary Tree Paths

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
     * @param root: the root of the binary tree
     * @return: all root-to-leaf paths
     */
    public List<String> binaryTreePaths(TreeNode root) {
        if (root == null) {
            return ans;
        }
        String prePath = "" + root.val;
        if (root.right == null && root.left == null){
            ans.add(prePath);
            return ans;
        }
        helper(root.left, prePath);
        helper(root.right, prePath);
        return ans;
    }

    private List<String> ans = new LinkedList<>();

    private void helper(TreeNode node, String prePath) {
        if (node == null) {
            return;
        }
        prePath += "->" + node.val;
        if (node.left == null && node.right == null) {
            ans.add(prePath);
            return;
        }
        helper(node.left, prePath);
        helper(node.right, prePath);
        return;
    }

}