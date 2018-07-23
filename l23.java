import java.util.Comparator;
import java.util.PriorityQueue;

// Merge k Sorted Lists

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        Comparator<ListNode> cmp = (n1, n2) -> Integer.compare(n1.val, n2.val);
        PriorityQueue<ListNode> queue = new PriorityQueue<>(cmp);
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;

        for (int i=0; i < lists.length; i++) {
            if (lists[i] != null) {
                queue.offer(lists[i]);
            }
        }

        while (!queue.isEmpty()) {
            ListNode node = queue.poll();
            cur.next = node;
            cur = cur.next;
            if (node.next != null) {
                queue.offer(node.next);
            }
        }
        return dummy.next;
    }
}