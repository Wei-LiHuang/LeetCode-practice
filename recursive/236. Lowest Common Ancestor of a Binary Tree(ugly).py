# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(cur: 'TreeNode', p: 'TreeNode', q: 'TreeNode', res: List['TreeNode']) -> bool:
            
            if cur.left is None and cur.right is None:
                if cur.val == p.val:
                    return True
                elif cur.val == q.val:
                    return True
                else:
                    return False
                
            findLeft = False
            if cur.left is not None:
                findLeft = dfs(cur.left, p, q, res)
                            
            findRight = False    
            if cur.right is not None:
                findRight = dfs(cur.right, p, q, res)
                
            if findLeft and findRight:
                res.append(cur)
                return True
            elif findLeft and (cur.val == q.val or cur.val == p.val):
                res.append(cur)
                return True
            elif findRight and (cur.val == q.val or cur.val == p.val):
                res.append(cur)
                return True       
            elif cur.val == q.val or cur.val == p.val:
                return True
            elif findLeft:
                return True
            elif findRight:
                return True
            
            return False
        
        res = []
        dfs(root, p, q, res)
        
        return res[0]
                
            
            
        
