class Solution:
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
    
        def reverse(lst, l, r):            
            while l < r:
                temp = lst[l]
                lst[l] = lst[r]
                lst[r] = temp
                l += 1
                r -= 1
            return
        
        if head is None:
            return None
                
        l = []
        
        shift = head
        while shift is not None:            
            l.append(shift)
            shift = shift.next
            
        listLength = len(l)
        
        if k > listLength:
            k = k % listLength
        
        reverse(l, 0, len(l) - 1)
        reverse(l, 0, k - 1)
        reverse(l, k, len(l) - 1)
        
        for i in range(0, len(l)):
            
            if i == len(l) - 1:
                l[i].next = None
            else:
                l[i].next = l[i + 1]
        
        return l[0]
        
        
