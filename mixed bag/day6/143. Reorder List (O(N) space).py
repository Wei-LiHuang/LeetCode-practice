# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head is None:
            return None
        
        nodes = []
        shift = head
        while shift is not None:
            _next = shift.next
            shift.next = None
            nodes.append(shift)
            shift = _next
            
        l, r = 0, len(nodes) - 1
        
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            
            if l == r:
                break
            
            nodes[r].next = nodes[l]
            r -= 1
            
        return nodes[0]
            
