"""Merge k Sorted Lists"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        curr = dummyhead
        while None in lists:
            lists.remove(None)
        tmp = []
        for i in range(len(lists)):
            tmp.append(lists[i].val)

        while lists:                     
            a = tmp.index(min(tmp))
            curr.next = lists[a] 
            curr = curr.next
            if lists[a].next:
                lists[a] = lists[a].next
                tmp[a] = lists[a].val
            else:
                lists.remove(lists[a])
                tmp.remove(tmp[a])

        return dummyhead.next
            
               
a = Solution()
print (a.mergeKLists([[]]))

# beat 6% people ...

"""
    this is the answer from other

    from Queue import PriorityQueue 

        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next   

"""

        
