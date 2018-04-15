""" Palindrome Linked List """

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True

        fast = head
        slow = head
        pre = None

        while fast:
            if not fast.next:
                break
            fast = fast.next.next
            
            nx = slow.next
            slow.next = pre
            pre = slow
            slow = nx
        
        if fast:
            slow = slow.next

        while slow:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        
        return True

