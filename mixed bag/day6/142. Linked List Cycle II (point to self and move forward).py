# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        def rec(cur, res):            
            
            if cur.next is None:
                return
            
            if cur.next is cur:
                res[0] = cur
                return
            
            #cur.next is not None:
            _next = cur.next
            cur.next = cur
            fromNext = rec(_next, res)        
            cur.next = _next
            
            return
        
        if head is None:
            return None
        
        res = [None]
        rec(head, res)
            
        return res[0]
            
            
            
