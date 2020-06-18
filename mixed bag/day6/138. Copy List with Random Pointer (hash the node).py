"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head is None:
            return None
        
        lst, ran, shift = [], [], head
        while shift is not None:
            lst.append([shift, shift.next, shift.random])
            shift = shift.next
            
        _dict = dict()
        
        for i in range(0, len(lst)):
            curNode = Node(lst[i][0].val, None, None)
            _dict[lst[i][0]] = curNode
            
        for i in range(0, len(lst)):            
            if lst[i][1] is None:
                _dict[lst[i][0]].next = None
            else:            
                _dict[lst[i][0]].next = _dict[lst[i][1]]
            
            if lst[i][2] is None:
                _dict[lst[i][0]].random = None
            else:
                _dict[lst[i][0]].random = _dict[lst[i][2]]
        
        return _dict[head]
