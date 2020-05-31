# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(node, res, isLeft):
            
            if not node.left and not node.right:
                if isLeft:
                    res[0] += node.val
                return
            
            if node.left:
                dfs(node.left, res, True)
            if node.right:
                dfs(node.right, res, False)
                
            return
        
        
        if not root:
            return 0
        
        res = [0]
        dfs(root, res, False)
        
        return res[0]
        
