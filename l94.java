import java.util.ArrayList;
import java.util.Stack;

// finition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
 
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        ArrayList<Integer> ansList = new ArrayList<>();
        TreeNode curr = root;

        while(curr != null || stack.size() != 0) {
            while(curr != null) {
                stack.add(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            ansList.add(curr.val);
            curr = curr.right;
        }
        return ansList;
    }
}