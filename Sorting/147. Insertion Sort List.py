# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# how to move a small value to its correct pos?
# need ask for better method

class Solution(object):
    
    def rec(self, cur):        
        
        if cur is None:                                    
            return None
                        
        node = self.rec(cur.next)
        
        if node is None: #cur is the last element.
            return cur        
        else:
            res = cur #next = node            
            while cur.val > node.val:
                cur.val, node.val = node.val, cur.val
                cur = cur.next
                node = node.next
                if node is None:
                    break
            return res
                                                        
    
    def insertionSortList(self, head):
        head = self.rec(head)
        return head
        
