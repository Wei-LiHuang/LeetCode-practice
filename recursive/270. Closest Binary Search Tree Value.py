# 1. find closest bigger and smaller, compare -> 2 * lg N -> X
# 2. recursive


class Solution:
    
    def closestValue(self, node: TreeNode, tgt: float) -> int:
        
        if node.left == None and node.right == None:
            return node.val
        
        d0 = abs(node.val - tgt)
        d1, d2 = d0 + 1, d0 + 1
                       
        minD = d0
        res = node.val
        
        if node.left:
            c1 = self.closestValue(node.left, tgt)
            d1 = abs(c1 - tgt)
            if d1 < minD:
                res = c1
                minD = d1
        
        if node.right:
            c2 = self.closestValue(node.right, tgt)
            d2 = abs(c2 - tgt)
            if d2 < minD:
                res = c2
                minD = d2
                
        
        return res
