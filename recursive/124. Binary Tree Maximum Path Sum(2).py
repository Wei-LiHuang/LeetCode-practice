# p0: self node as path root 
#       -> a. self
#          b. self + leftPath(no fork)
#          c. self + rightPth(no fork)
#          d: self + leftPath(no fork) + rightPath(no fork)
# p1: left node as path root
# p2: right node as path root


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:        
        
        def dfs(node, res): #return [pa, pb, pc]
            
            if node.left is None and node.right is None:
                res[0] = max(res[0], node.val)
                return [node.val, node.val, node.val]
            
            fromRight, fromLeft = [0, 0, 0], [0, 0, 0]
            pa, pb, pc, pd = node.val, node.val, node.val, node.val 
            if node.left is not None:
                fromLeft = dfs(node.left, res)
                pb += max(fromLeft)
                pd += max(fromLeft)
                
            if node.right is not None:
                fromRight = dfs(node.right, res)
                pc += max(fromRight)
                pd += max(fromRight)
                
                
            res[0] = max([res[0], pa, pb, pc, pd])
            
            return [pa, pb, pc]
        
        
        if root is None:
            return 0
        
        res = [-float('inf')]
        dfs(root, res)
        
        return res[0]
