import java.util.ArrayList;
import java.util.Stack;

import javafx.scene.transform.Rotate;

/**
 * Definition for a binary tree node.
 * */
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
 
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> ans = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        if(root == null){
            return ans;
        }
        stack.add(root);
        while(stack.size() != 0) {            
            curr = stack.pop();
            ans.add(curr.val);
            if(curr.right != null) stack.add(curr.right);
            if(curr.left != null) stack.add(curr.left);        
        }
        return ans;
    }
}