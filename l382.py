import random

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.total = 0
        self.head = head
        cur = head
        while head.next is not None:
            self.total += 1
            cur = cur.next



    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        leap = random.randint(0, self.total)
        i = 0
        cur = self.head
        while i < leap:
            cur = cur.next
            i += 1
        return cur.val






# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
