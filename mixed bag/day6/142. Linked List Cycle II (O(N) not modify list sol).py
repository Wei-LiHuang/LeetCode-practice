class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        slow = head
        fast = head
        
        intersect = None
        while fast is not None and fast.next is not None:                                                
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                intersect = slow
                break
        
        if intersect is None:
            return None
                                        
        while head is not slow:
            slow = slow.next
            head = head.next
                                
        return slow
