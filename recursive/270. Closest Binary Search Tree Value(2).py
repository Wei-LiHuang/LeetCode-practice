# 1. find closest bigger and smaller, compare -> 2 * lg N -> X
# 2. recursive

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        def dfs(node, tgt, res):
            
            if not node.left and not node.right:     
                if not res[2] or res[0] > abs(tgt - node.val):
                    res[0] = abs(tgt - node.val)
                    res[1] = node.val
                    res[2] = True                                
                return
            
            if node.left:
                dfs(node.left, tgt, res)
                
            if node.right:
                dfs(node.right, tgt, res)
                
            if not res[2] or res[0] > abs(tgt - node.val):
                    res[0] = abs(tgt - node.val)
                    res[1] = node.val
                    res[2] = True                                
            return
        
        
        res = [0, None, False]
        dfs(root, target, res)
        
        return res[1]
