import java.util.*;

public class ReverseHalfLL {
	public void reverse(Node head) {
        if (head == null || head.next == null) {
            return;
        }

        Node slow = head;
        Node fast = head;

        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        Node secondHead = slow;

        Node cur = slow.next;
        Node pre = null;

        while (cur != null) {
            Node next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next; 
        }

        secondHead.next = pre;

	}

	static class Node {
		private int val;
		private Node next;

		public Node(int val, Node node) {
			this.val = val;
			next = node;
		}
	}

	public String printLL(Node node) {
		StringBuilder res = new StringBuilder();
		Node curr = node;
		while(curr != null) {
			res.append(curr.val).append(",");
			curr = curr.next;
		}
		return res.toString();
	}

	public static void main(String[] args) {
		ReverseHalfLL test = new ReverseHalfLL();
		Node head = new Node(1, null);
		Node node = head;
		for (int i = 2; i < 6; i++) {
			node.next = new Node(i, null);
			node = node.next;
		}
		System.out.println(test.printLL(head));
		test.reverse(head);
		System.out.println(test.printLL(head));

	}
}