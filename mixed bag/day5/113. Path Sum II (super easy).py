# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, tgt: int) -> List[List[int]]:
        
        def dfs(cur, tgt, _sum, path, res):
            
            if cur.left is None and cur.right is None:
                if _sum + cur.val == tgt:
                    path.append(cur.val)
                    res.append(list(path))
                    path.pop()
                
                return 
            
            
            path.append(cur.val)
            
            if cur.left is not None:                
                dfs(cur.left, tgt, _sum + cur.val, path, res)                
            
            if cur.right is not None:                
                dfs(cur.right, tgt, _sum + cur.val, path, res)
                
            path.pop()
            
            
            return 
        
        
        path, res = [], []
        
        if root is None:
            return []
        
        dfs(root, tgt, 0, path, res)
        
        return res
        
