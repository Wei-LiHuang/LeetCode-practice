# should use iterative
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        def rec(cur, pre, count):

            r = None
            if cur.next is not None:
                r = rec(cur.next, cur, count + 1)
            else:
                r = cur
            
            if count % 2 == 0:
                return r
            
            elif count % 2 == 1:
                
                if cur.next is not None:
                    pre.next = r
                else:
                    pre.next =  None
                    
                cur.next = pre       
                
            return cur
        
        if head is None:
            return head
        
        head = rec(head, None, 0)
        
        return head
