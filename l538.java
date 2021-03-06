// 538. Convert BST to Greater Tree
import java.util.ArrayDeque;

import java.util.Deque;


public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null){
            return null;
        }
        ListNode cur;
        cur = headA;
        while (cur.next != null){
            cur = cur.next;
        }
        cur.next = headB;

        ListNode fast = headA;
        ListNode slow = headA;

        while (fast!=null && fast.next!=null){
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow){
                ListNode slow2 = headA;
                while (slow2 != slow){
                    slow = slow.next;
                    slow2 = slow2.next;
                }
                cur.next = null;
                return slow;
            }
        }
        cur.next = null;
        return null;

    }
}


// 538. Convert BST to Greater Tree



public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
 }


public class Solution {
    public TreeNode convertBST(TreeNode root) {

        Deque<TreeNode> stack = new ArrayDeque<TreeNode>();
        TreeNode cur = root;
        int total = 0;

        while (!stack.isEmpty() || cur != null){
            while (cur != null){
                stack.push(cur);
                cur = cur.right;
            }
            TreeNode top = stack.poll();
            total += top.val;
            top.val = total;
            cur = top.left;
        }
        return root;
    }
}
