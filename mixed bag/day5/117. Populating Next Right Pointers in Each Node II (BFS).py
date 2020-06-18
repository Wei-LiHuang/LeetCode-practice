"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
                
        if root is None:
            return None
        
        q = collections.deque()
        q.appendleft(root)
        
        while len(q) > 0:
            curSize = len(q)
            level = collections.deque()
            for i in range(0, curSize):
                cur = q.pop()               
                if cur is not None:
                    if cur.right is not None:
                        level.appendleft(cur.right)
                    if cur.left is not None:
                        level.appendleft(cur.left)
                        
            for j in range(0, len(level) - 1):
                level[j].next = level[j + 1]
                
            q = level
            
        return root
                
                
                    
