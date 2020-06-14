# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def found(node, p, q, res):
            
            if node.left is None and node.right is None:
                if node.val == p.val:
                    return True
                if node.val == q.val:
                    return True
                return False
            
            fromLeft, fromRight = False, False
            
            ret = False
            count = 0            
            if node.val == p.val or node.val == q.val:
                count += 1
                ret = True
            
            if node.left is not None:
                fromLeft = found(node.left, p, q, res)
                if fromLeft:
                    if count == 1:
                        res[0] = node                        
                    else:                        
                        count += 1
                        ret = True
                    
            if node.right is not None:
                fromRight = found(node.right, p, q, res)
                if fromRight:
                    if count == 1:
                        res[0] = node
                    else:                        
                        count += 1
                        ret = True
                        
            return ret
        
        
        res = [None]
        found(root, p, q, res)
        
        return res[0]
            
            
