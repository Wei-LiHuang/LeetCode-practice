# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        def rec(cur, tgt):
            
            if cur.next is None:
                if cur.val == tgt:
                    return None
                else:
                    return cur
            
            fromNext = rec(cur.next, tgt)
            if cur.val == tgt:
                return fromNext
            else:
                cur.next = fromNext
                return cur
            
            
        if head is None:
            return None
        
        return rec(head, val)
            
