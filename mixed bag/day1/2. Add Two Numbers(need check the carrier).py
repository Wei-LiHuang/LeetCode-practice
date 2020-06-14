# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 2-> 4-> 3 + 5 -> 6 -> 4 = 342 + 465 = 807
# no leading zero, except zero itself.

# brute force: traverse each link list, get the number, and add them, then turn back to linked list.
# runtime: O(max(l1, l2)). space O(max(l1, l2))

# or use recursive:
# 32 = 2 -> 3, 108 = 8 -> 0 -> 1
# 32 + 108 = 140 = 0 -> 4 -> 1
# (2, 8), 0 -> 10 -> listNode(0), carrier = 1
# (3, 0), 1 -> 4 -> listNode(4), carrier = 0
# (null, 1), 0 -> 1 -> listNode(1), carrier = 0
# (null, null) -> return XXXXXXXXX -> need check carrier !!!!!!!!!!

# runtime: O(max(l1, l2)). space O(max(l1, l2))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
                
        def rec(n1, n2, carrier, parent):
            
            if n1 is None and n2 is None:
                if carrier == 1:
                    parent.next = ListNode(1, None)
                return
            
            v1, v2 = 0, 0
            next1, next2 = None, None
            
            if n1 is not None:
                v1 = n1.val
                next1 = n1.next
            if n2 is not None:
                v2 = n2.val
                next2 = n2.next
                
            vAdd = v1 + v2 + carrier
            
            newV, newCarrier = 0, 0
            if vAdd >= 10:
                newCarrier = 1
                newV = vAdd - 10
            else:
                newCarrier = 0
                newV = vAdd
                
            node = ListNode(newV, None)
            parent.next = node
                                                
            rec(next1, next2, newCarrier, node)
            
            return
                
        dummy = ListNode(-1, None)                
        rec(l1, l2, 0, dummy)
        return dummy.next
            
