"""Copy List with Random Pointer"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        # """
        # if head is None:
        #     return None
        # ocurr = head
        # newhead = RandomListNode(head.label)
        # ncurr = newhead
        # looktable = {head:newhead, None:None}
        # while ocurr.next is not None:
        #     ncurr.next = RandomListNode(ocurr.next.label)
        #     ncurr = ncurr.next
        #     ocurr = ocurr.next
        #     looktable[ocurr] = ncurr
        # ocurr = head
        # ncurr = newhead
        # while ocurr is not None:
        #     ncurr.random = looktable[ocurr.random]
        #     ncurr = ncurr.next
        #     ocurr = ocurr.next
        # return newhead

        if head is None:
            return None
        curr = head
        mapdic = {None:None}
        while curr:
            mapdic[curr] = RandomListNode(curr.label)
            curr = curr.next
        curr = head
        while curr:
            mapdic[curr].next = mapdic[curr.next]
            mapdic[curr].random = mapdic[curr.random]
            curr = curr.next
        return mapdic[head]

        



        

