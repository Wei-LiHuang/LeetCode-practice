# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# if the list has cycle => fast will catech up eventually
# so the slow and fast can all be set to the head at the begining as long as the step is different
# (but needs to add a condiction slow is fast and slow is not head in line 23)
# the fast can also taking three step at each loop, but need to be careful to the consequences using this in len = 2 list.

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head or not head.next:            
            return False
        
        slow, fast = head, head.next
        
        while slow is not fast:                        
            if not fast or not fast.next:
                return False            
            else:
                fast = fast.next.next
                slow = slow.next

        return True
        
        
