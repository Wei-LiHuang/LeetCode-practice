# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def rec(self, node, count):
        
        if node.next is None:
            count[0] -= 1
            if count[0] == 0:
                return None
            else:
                return node
                    
        node.next = self.rec(node.next, count)
        
        if count[0] >= 0:
            count[0] -= 1
        
        if count[0] == 0:
            return node.next        
        else:
            return node                    
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = [n]
        head = self.rec(head, count)
        return head
