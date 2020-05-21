# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, a, b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """                        
        n1 = a
        n2 = b
        
        if a is None or b is None:
            return None
        
        while n1 is not n2:
            n1 = n1.next
            n2 = n2.next                        
            
            if n1 is None:
                if b is None:
                    return None
                else:
                    n1 = b
                    b = None
            
            if n2 is None:
                if a is None:
                    return None
                else:
                    n2 = a            
                    a = None
                    

                                                
        return n1
