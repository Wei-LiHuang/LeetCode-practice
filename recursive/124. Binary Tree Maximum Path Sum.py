# for leaf node: update res by node.val, return node.val
#
# for one child node: 
#   update res by:
#       p1 = only use node, (p2, p3) = use node and childPath, (p5, p6) = not include current node
#   return:
#       max(p1, p2\p3) ... must include current node
# for two children node:
#   update res by:
#       p1 = only use node, (p2, p3) = use node and childPath, p4 = node + leftchildPath + rightChildPath, (p5, p6) = not include current node
#   return:
#       max(p1, p2\p3) ... must include current node and can only use one side (can't fork path)

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        
        def dfs(node, res):
            
            p1, p2, p3, p4, p5, p6 = node.val, 0, 0, 0, 0, 0
            
            if not node.left and not node.right:
                res[0] = max(res[0], p1)
                return p1
                        
            elif not node.right and (node.left):
                fromLeft = dfs(node.left, res)                
                p2 = node.val + fromLeft
                p5 = fromLeft
                returnRes = max(p1, p2)
                maxPath = max(returnRes, p5) 
                res[0] = max(res[0], maxPath)
                return returnRes
                
            elif not node.left and node.right:
                fromRight = dfs(node.right, res)                
                p3 = node.val + fromRight
                p6 = fromRight
                returnRes = max(p1, p3)
                maxPath = max(returnRes, p6) 
                res[0] = max(res[0], maxPath)
                return returnRes
                
            elif node.left and node.right:
                fromLeft = dfs(node.left, res)                                
                fromRight = dfs(node.right, res)
                p2 = node.val + fromLeft                
                p3 = node.val + fromRight
                p4 = node.val + fromLeft + fromRight
                p5 = fromLeft
                p6 = fromRight
                
                returnRes = max([p1, p2, p3])
                maxPath = max([returnRes, p5, p6]) 
                res[0] = max([res[0], maxPath, p4])
                return returnRes
            
        
        res = [root.val]
        dfs(root, res)
        return res[0]
