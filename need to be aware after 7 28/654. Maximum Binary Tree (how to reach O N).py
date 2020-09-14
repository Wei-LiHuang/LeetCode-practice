# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, a: List[int]) -> TreeNode:                
        n = len(a)
        for i in range(0, n):
            a[i] = TreeNode(a[i], None, None)
            
        q = collections.deque()
        
        for i in range(0, n):
            cur = a[i]
            
            while len(q) > 0 and q[-1].val < cur.val:
                cur.left = q.pop()
                
            if len(q) != 0:
                q[-1].right = cur
            
            q.append(cur)
            
        
        if len(q) == 0:
            return None
        
        return q[0]
                
