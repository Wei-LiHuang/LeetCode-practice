# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# traverse to the end node and start to do n-1. If n reaches 0, node cur = cur.next
# Given n will always be valid => n > 0

#edge case->the head node is the node need to remove: use dummy


class Solution(object):
    
    def recur (self, cur, n):
        
        if cur.next is None:             
            return n - 1
            
        else:
            count = self.recur(cur.next, n)
            if count == 0:       
                cur.next = cur.next.next
                return -1
            elif count == -1:
                return -1
            else:
                return count - 1
            
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)        
        dummy.next = head
        self.recur(dummy, n)               
        return dummy.next
