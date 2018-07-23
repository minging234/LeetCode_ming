// Convert Sorted List to Binary Search Tree

/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
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
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
 
        ListNode midNode = findMid(head);
        TreeNode treeNode = new TreeNode(midNode.val);

        if (head != midNode) treeNode.left = sortedListToBST(head);
        treeNode.right = sortedListToBST(midNode.next);
        return treeNode;
    }

    private ListNode findMid(ListNode node) {
        if (node == null) return null;
        ListNode fast = node;
        ListNode slow = node;
        ListNode pre = null;

        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            pre = slow;
            slow = slow.next;
        }
        if (pre != null) pre.next = null;

        return slow;
    }
}




// method that did not change the original list structure

// public class Solution {
//     private ListNode current;

//     private int getListLength(ListNode head) {
//         int size = 0;

//         while (head != null) {
//             size++;
//             head = head.next;
//         }

//         return size;
//     }

//     public TreeNode sortedListToBST(ListNode head) {
//         int size;

//         current = head;
//         size = getListLength(head);

//         return sortedListToBSTHelper(size);
//     }

//     public TreeNode sortedListToBSTHelper(int size) {
//         if (size <= 0) {
//             return null;
//         }

//         TreeNode left = sortedListToBSTHelper(size / 2);
//         TreeNode root = new TreeNode(current.val);
//         current = current.next;
//         TreeNode right = sortedListToBSTHelper(size - 1 - size / 2);

//         root.left = left;
//         root.right = right;

//         return root;
//     }
// }