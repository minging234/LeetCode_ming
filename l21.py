#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        que1 = l1
        que2 = l2
        head = ListNode(0)
        cur = head

        while que1 and que2:
            if que1.val >= que2.val:
                cur.next = que2
                que2 = que2.next
            elif que1.val < que2.val:
                cur.next = que1
                que1 = que1.next
            cur = cur.next
        if que2 is None:
            cur.next = que1
        else:
            cur.next = que2

        return head.next

