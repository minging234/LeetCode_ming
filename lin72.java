import java.util.ArrayList;

// Construct Binary Tree from Inorder and Postorder 

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
     * @param inorder: A list of integers that inorder traversal of a tree
     * @param postorder: A list of integers that postorder traversal of a tree
     * @return: Root of a tree
     */

    private int ind = 0;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.ind = postorder.length;
        return helper(inorder,0,inorder.length - 1, postorder);   
    }

    private TreeNode helper(int[] inorder, int start, int end, int[] postorder) {
        if (start > end) return null;
        this.ind --;
        TreeNode node = new TreeNode(postorder[this.ind]); 
        int position = findPosition(inorder, start, postorder[this.ind]);
        node.right = helper(inorder, position + 1, end, postorder);
        node.left = helper(inorder, start, position - 1, postorder);
        return node;
    }


    private int findPosition(int[] a, int start, int b) {
        for (int i=start; i < a.length; i++) {
            if (a[i] == b) {
                return i;
            }
        }
        return -1;
    }
}

// the method without a global variable

// public class Solution {
//     private int findPosition(int[] arr, int start, int end, int key) {
//         int i;
//         for (i = start; i <= end; i++) {
//             if (arr[i] == key) {
//                 return i;
//             }
//         }
//         return -1;
//     }

//     private TreeNode myBuildTree(int[] inorder, int instart, int inend,
//             int[] postorder, int poststart, int postend) {
//         if (instart > inend) {
//             return null;
//         }

//         TreeNode root = new TreeNode(postorder[postend]);
//         int position = findPosition(inorder, instart, inend, postorder[postend]);

//         root.left = myBuildTree(inorder, instart, position - 1,
//                 postorder, poststart, poststart + position - instart - 1);
//         root.right = myBuildTree(inorder, position + 1, inend,
//                 postorder, poststart + position - instart, postend - 1);
//         return root;
//     }

//     public TreeNode buildTree(int[] inorder, int[] postorder) {
//         if (inorder.length != postorder.length) {
//             return null;
//         }
//         return myBuildTree(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
//     }
// }