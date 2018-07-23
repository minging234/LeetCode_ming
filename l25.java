/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null) return head;
        
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode end = head;
        ListNode start = dummy;
        int count = 0;

        while (end != null) {
            count ++;
            if (count == k) {
                ListNode pre = end.next;
                ListNode cur = start.next;
                
                start.next = end;
                start = cur;
                end = end.next;

                while (count > 0) {
                    ListNode nextNode = cur.next;
                    cur.next = pre;
                    pre = cur;
                    cur = nextNode;
                    count --;
                }

                continue;
            }
            end = end.next;
        }

        return dummy.next;
    }
}