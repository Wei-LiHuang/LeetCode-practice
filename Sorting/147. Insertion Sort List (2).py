# insertion sort: N^2

class Solution:
    
    
    def rec(self, cur):
        
        if cur.next is None:
            return cur
        
        nxt = self.rec(cur.next)                
        cur.next = nxt
        
        shift = nxt        
        res = cur        
        while shift is not None and shift.val < cur.val:
            cur.val, shift.val = shift.val, cur.val
            cur = shift
            shift = shift.next
            
        return res
                
    
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        head = self.rec(head)
        return head
        
            
            
