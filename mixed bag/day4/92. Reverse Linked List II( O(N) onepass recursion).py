# O(N), one pass recursion

class Solution:
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
                
        def rec(cur, l, r):               
            if r > 0:
                fromNext = rec(cur.next, l - 1, r - 1)                
            elif r == 0:       
                tail = cur.next
                cur.next = None
                return [cur, cur, tail]
            
            
            swapHead = fromNext[0]
            swapTail = fromNext[1]
            tail = fromNext[2]                     
            
            if l <= 0:       
                swapTail.next = cur
                cur.next = None
                return [swapHead, cur, tail]
            
            if l > 0:
                cur.next = swapHead
                return [cur, swapTail, tail]
                                            
        #return rec(head, m, n)
        res = rec(head, m  - 1, n - 1)
        res[1].next = res[2]
        
        return res[0]
        
