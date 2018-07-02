// Binary Search Tree Iterator

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
 * Example of iterate a tree:
 * BSTIterator iterator = new BSTIterator(root);
 * while (iterator.hasNext()) {
 *    TreeNode node = iterator.next();
 *    do something for node
 * } 
 */


public class BSTIterator {
    /*
    * @param root: The root of binary tree.
    */public BSTIterator(TreeNode root) {
        // do intialization if necessary
        this.curr = root;
        if (!this.stack.isEmpty() || this.curr != null) {
            while (this.curr != null) {
                this.stack.push(this.curr);
                this.curr = this.curr.left;
            }
        }
        this.curr = this.stack.pop();
    }

    Stack<TreeNode> stack = new Stack<>();

    TreeNode curr = null;

    /*
     * @return: True if there has next node, or false
     */
    public boolean hasNext() {
        // write your code here
        if (this.curr == null && this.stack.isEmpty()) return false;
        return true;
    } 

    /*
     * @return: return next node
     */
    public TreeNode next() {
        // write your code here
        TreeNode ans = this.curr;
        this.curr = this.curr.right;
        if (hasNext()){
            while (this.curr != null) {
                this.stack.push(this.curr);
                this.curr = this.curr.left;
            }
            this.curr = this.stack.pop();
        }
        return ans;
    }
}