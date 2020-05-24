# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA is None or headB is None:
            return None
        
        n1 = headA
        n2 = headB                        
        while n1 is not n2:
            
            n1 = n1.next            
            if n1 is None:
                n1 = headB
                headB = None

            n2 = n2.next
            if n2 is None:
                n2 = headA
                headA = None
                
            if n1 is None or n2 is None:
                return None
            
        return n1
        
        
