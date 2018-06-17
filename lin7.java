import java.util.LinkedList;
import java.util.Queue;

// Serialize and Deserialize Binary Tree

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
     * This method will be invoked first, you should design your own algorithm 
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    public String serialize(TreeNode root) {
        // BFS
        if (root == null) {
            return "#";
        }
        
        Queue<TreeNode> que = new LinkedList<>();

        String ans = "" + root.val;
        que.add(root.left);
        que.add(root.right);

        while (!que.isEmpty()) {
            TreeNode curr = que.poll();
            
            if (curr == null) {
                ans += ",#";
                continue;
            } 

            ans += "," + curr.val; 
            que.add(curr.left);
            que.add(curr.right);

        }

        return ans;
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in 
     * "serialize" method.
     */
    public TreeNode deserialize(String data) {
        // BFS recover
        if (data.equals("#")) return null;

        String[] vals = data.split(",");

        boolean isLeft = true;
        Queue<TreeNode> que = new LinkedList<>();
        TreeNode root = new TreeNode(Integer.parseInt(vals[0]));
        TreeNode curr = root;
        que.add(root);

        for (int i=1; i < vals.length; i++) {
            if (isLeft) {
                curr = que.poll();
            }
            if (!vals[i].equals("#")) {
                TreeNode tail = new TreeNode(Integer.parseInt(vals[i]));

                if (isLeft) {
                    curr.left = tail;
                } else {
                    curr.right = tail;
                }
                que.add(tail);
            }
            isLeft = !isLeft;
        }

        return root;
    }
}