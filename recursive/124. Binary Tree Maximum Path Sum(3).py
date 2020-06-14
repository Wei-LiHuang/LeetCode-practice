# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        #res = [maxPathSum]
        def dfs(cur, res):            
            if cur.left is None and cur.right is None:
                res[0] = max(res[0], cur.val)
                return cur.val
            
            fromLeft, fromRight = 0, 0
            
            if cur.left is not None:
                fromLeft = dfs(cur.left, res)
                
            if cur.right is not None:
                fromRight = dfs(cur.right, res)
                
            res[0] = max([res[0], cur.val, cur.val + fromLeft, cur.val + fromRight, cur.val + fromLeft + fromRight])
            
            return max(cur.val, cur.val + fromLeft, cur.val + fromRight)
        
        
        res = [-float('inf')]
        dfs(root, res)
        
        return res[0]
                
