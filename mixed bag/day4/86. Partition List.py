# 1->4->3->2->5->2, x = 3
# 1->2->2->4->3->5

# use two header to record the elements, link both list at the end


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        def rec (h1, h2, cur, x, dummy1):
            
            if cur is None:
                h2.next = dummy1.next
                return
            
            _next = cur.next
            
            if cur.val >= x:                
                h1.next = cur            
                h1.next.next = None
                rec(h1.next, h2, _next, x, dummy1)
            else:
                h2.next = cur
                h2.next.next = None
                rec(h1, h2.next, _next, x, dummy1)
                
            return
            
                                                                                                    
        if head is None or head.next is None:
            return head
        
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
                        
        rec(dummy1, dummy2, head, x, dummy1)
                                        
        return dummy2.next
