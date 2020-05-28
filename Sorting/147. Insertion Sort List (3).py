# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        def rec(cur):
            
            if cur.next is None:
                return cur            
            else:
                node = rec(cur.next)
                
                if cur.val > node.val:
                    s1 = cur
                    s2 = node
                    while s2.val < s1.val:
                        s2.val, s1.val = s1.val, s2.val
                        s1 = s2
                        s2 = s2.next
                        if s2 is None:
                            break
                
                cur.next = node
                return cur
            
            
        if head is None:
            return None
        
        return rec(head)
                
                
                
