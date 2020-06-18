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
        
        shift, lst = head, []
        while shift is not None:            
            lst.append(shift)
            copied = Node(shift.val, None, None)            
            temp = shift.next
            shift.next = copied 
            lst.append(copied)
            shift = temp
                
        res, i = lst[1], 0        
        while i < len(lst):                            
            curOldNode = lst[i]
            curCopied = lst[i + 1]
            
            if i + 1 + 2 >= len(lst):
                curCopied.next = None
            else:
                curCopied.next = lst[i + 1 + 2]            
                
            if curOldNode.random is None:
                curCopied.random = None
            else:
                curCopied.random = curOldNode.random.next
            
            i += 2
            
        return res
            
        
