# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        def rec(node, count):

            if node.next is None:
                count[0] -= 1
                if count[0] == 0:
                    return None
                else:
                    return node

            node.next = rec(node.next, count)

            if count[0] >= 0:
                count[0] -= 1

            if count[0] == 0:
                return node.next        
            else:
                return node                    
    
            
            
        head = rec(head,[n])
        
        return head
            
        
        
        
