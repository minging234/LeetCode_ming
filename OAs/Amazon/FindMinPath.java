//  Binary search tree minimum sum from root to leaf


public class FindMinPath {
	public int getMinSum(Node root) {
        if (root == null) {
            return 0;
        }
        // if (root.left == null && root.right != null) {
        //     return getMinSum(root.right) + root.val;
        // }
        // if (root.left != null && root.right == null) {
        //     return getMinSum(root.left) + root.val;
        // }
        return Math.min(getMinSum(root.left), getMinSum(root.right)) + root.val;
	}


	static class Node {
		int val;
		Node left;
		Node right;

		public Node(int val, Node left, Node right) {
			this.val = val;
			this.left = left;
			this.right = right;
		}
	}

	public static void main(String[] args) {
		FindMinPath test = new FindMinPath();
		Node root = new Node(3, new Node(2, new Node(-10, null, null), null), new Node(4, null, null));
		System.out.println(test.getMinSum(root));
	}
}