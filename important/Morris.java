import java.util.ArrayList;

// Morris method to Inorder Traversal with O(1) space

public class Morris {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;

        while(root != null) {
            if (root.left != null) {
                cur = root.left;
                while (cur.right != null && cur.right != root) {
                    cur = cur.right;
                }

                if (cur == root) {
                    nums.add(root.val);
                    cur.right = null;
                    root = root.right;
                } else {
                    cur.right = root;
                    root = root.left;
                }

            } else {
                nums.add(root.val);
                root = root.right;
            }
        }

        return nums;

    }
}