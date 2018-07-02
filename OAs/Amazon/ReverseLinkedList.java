
// Reverse Linked List II

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) {
            return head;
        }
        
        int pos = 0;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        head = dummyHead;
        
        // move the pointer to the one before reversing
        while (pos < m -1) {
            head = head.next;
            pos += 1;
        }
   
        // preserve the gap
        ListNode pre = head.next;
        ListNode cur = pre.next;
        
        // reverse the link from m to n
        while (pos < n) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
            pos += 1;
        }
        
        head.next.next = cur;
        head.next = pre;
        head = dummyHead.next;
        return head;
    }
}