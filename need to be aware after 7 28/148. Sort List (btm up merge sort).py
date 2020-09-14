# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
            
        if head is None:
            return None
                  
        # get size:
        n = 0
        shift = head
        while shift is not None:            
            shift = shift.next
            n += 1

        # split the list into two list, return the second part head
        def split(head, _len):
            
            shift = head
            i = 1            
            while i < step and shift is not None:
                shift = shift.next
                i += 1
                
            if shift is None:
                return None
            
            temp = shift.next
            shift.next = None
            return temp
        
        def merge(h1, h2, head):
            shift = head
            while h1 is not None and h2 is not None:
                if h1.val < h2.val:
                    shift.next = h1
                    h1 = h1.next                    
                else:
                    shift.next = h2
                    h2 = h2.next
                shift = shift.next
            if h1 is not None:
                shift.next = h1
            if h2 is not None:
                shift.next = h2
                    
            while shift.next is not None:
                shift = shift.next            
            return shift
                
                    
            
        dummy = ListNode(-1)
        dummy.next = head
        l, r, tail = None, None, None
        
        step = 1
        while step < n:
            shift = dummy.next
            tail = dummy
            
            while shift is not None:
                l = shift
                r = split(l, step)                                            
                shift = split(r, step)
                tail = merge(l, r, tail)
                
                #print([l, r, shift, tail])
                
            step *= 2
        return dummy.next                    
        
