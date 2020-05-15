# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use hash set to store the path start from a, and then traverse b and checking the set look for the same node.

class Solution(object):
    def getIntersectionNode(self, h1, h2):
                
        _set = set()
        
        while h1 is not None:
            _set.add(h1)
            h1 = h1.next
            
        while h2 is not None:
            if h2 in _set:
                return h2
            h2 = h2.next
            
        return None
        
