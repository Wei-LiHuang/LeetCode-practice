# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def dfs(n1, n2):
            
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False
                                    
            if n1.val != n2.val:
                return False
            
            if dfs(n1.left, n2.left):
                
                if dfs(n1.right, n2.right):
                    return True
                else:
                    return False                
            else:
                return False
            
        
            return True
        
        return dfs(p, q)
