# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(node, isLeft, res):
            
            if not node.left and not node.right:
                if isLeft:
                    res[0] += node.val
                return
            
            if node.left:
                dfs(node.left, True, res)
            
            if node.right:
                dfs(node.right, False, res)
                
            return
        
        res = [0]
        if root:
            dfs(root, False, res)
        
        return res[0]
            
