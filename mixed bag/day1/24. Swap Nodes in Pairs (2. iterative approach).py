    def swapPairs(self, head: ListNode):
        
        if head is None or head.next is None:
            return head     
        
        p1, p2 = head, head.next
        
        head = p2
        tail = None
        while p1 is not None and p2 is not None:
            nextStart = p2.next
            p2.next = p1
            p1.next = nextStart
            
            if tail is not None:
                tail.next = p2
                        
            tail = p1                                    
            p1 = nextStart
            if p1 is None:
                break
            p2 = p1.next
                                                                            
        return head
