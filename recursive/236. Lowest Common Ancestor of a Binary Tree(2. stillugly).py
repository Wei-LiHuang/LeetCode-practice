# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            
            if not node.left and not node.right:
                if node.val == p.val or node.val == q.val:
                    return [1, None]            
                else:
                    return [0, None]
                
            fromLeft, fromRight = [0, None], [0, None]
            if node.left:
                fromLeft = dfs(node.left, p, q)            
                if fromLeft[0] == 2:
                    return fromLeft
                                                    
            if node.right:
                fromRight = dfs(node.right, p, q)
                if fromRight[0] == 2:
                    return fromRight
                                                            
            if fromLeft[0] == 1 and fromRight[0] == 1:
                return [2, node]
            
            if fromLeft[0] == 1:
                if node.val == p.val or node.val == q.val:
                        return [2, node]
                else:
                    return fromLeft
                
            if fromRight[0] == 1:
                if node.val == p.val or node.val == q.val:
                    return [2, node]            
                else:
                    return fromRight
                
            if node.val == p.val or node.val == q.val:
                    return [1, None]
            
            return [0, None]
        
        
        
        res = dfs(root, p, q)        
        return res[1]
                
        
