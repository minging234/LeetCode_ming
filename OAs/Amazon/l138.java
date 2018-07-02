import java.util.HashMap;

// Copy List with Random Pointer

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }
        HashMap<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode curr = head;
        while (curr != null) {
            RandomListNode copyedNode = new RandomListNode(curr.label);
            map.put(curr, copyedNode);
            curr = curr.next;
        }

        curr = head;

        while (curr != null) {
            RandomListNode node = map.get(curr);
            node.next = map.get(curr.next);
            node.random = map.get(curr.random);
            curr = curr.next; 
        }

        return map.get(head);
    }
}