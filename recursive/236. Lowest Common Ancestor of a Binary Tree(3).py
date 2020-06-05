# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p , q, res):
                        
            if not node.left and not node.right:
                if node.val == p.val:
                    return node
                if node.val == q.val:                
                    return node
                return None
                
            fromLeft, fromRight = None, None
            
            if node.left:
                fromLeft = dfs(node.left, p, q, res)

            if node.right:
                fromRight = dfs(node.right, p, q, res)
                
            #from left and from right:
            if fromLeft and fromRight:
                res[0] = node
                return node
            
            if fromLeft:
                if node.val == q.val or node.val == p.val:
                    res[0] = node
                    return node
                else:
                    return fromLeft
                
            if fromRight:
                if node.val == q.val or node.val == p.val:
                    res[0] = node
                    return node
                else:
                    return fromRight         
                
            if node.val == q.val or node.val == p.val:
                return node
                
            
            return None
            
                    
                                                                
        res = [None]
        dfs(root, p, q, res)
        
        return res[0]
                
