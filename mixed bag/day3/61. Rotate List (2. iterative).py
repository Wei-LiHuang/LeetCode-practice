    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head is None:
            return head
        
        shift = head                
        
        #get len:
        _len = 0
        while shift is not None:
            _len += 1
            shift = shift.next
               
        if k >= _len:
            k = k % _len
            
        if _len <= 1 or k == 0:
            return head
        
        breakPointIndex = _len - 1 - k
        count = 0
        shift = head
        newHead = None        
        while count < breakPointIndex:
            shift = shift.next
            count += 1
            
        newHead = shift.next
        shift.next = None
          
        shift = newHead
        while shift is not None:            
            if shift.next is None:
                shift.next = head
                break
            shift = shift.next
        
        return newHead
