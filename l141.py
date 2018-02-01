""" Linked List Cycle """

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ndic = {}
        while head is not None:
            if head in ndic:
                return True
            ndic[head] = 1
            head = head.next
        return False