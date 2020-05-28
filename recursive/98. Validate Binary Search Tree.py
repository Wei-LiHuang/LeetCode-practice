# need to check subTree min and max
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        def dfs(node: TreeNode):
            
            if node.left is None and node.right is None:
                return [True, node.val, node.val]
                                    
            minVal, maxVal = node.val, node.val
            
            if node.left:                
                fromLeft = dfs(node.left)
                if not fromLeft[0]:
                    return [False, node.val, node.val]
                else:
                    c1 = node.val > node.left.val
                    c2 = fromLeft[1] < node.val
                    if not c1 or not c2:
                        return [False, node.val, node.val]
                    
                    minVal = min(minVal, fromLeft[2])
                                
            if node.right:
                fromRight = dfs(node.right)
                if not fromRight[0]:
                    return [False, node.val, node.val]
                else:
                    c1 = node.val < node.right.val
                    c2 = fromRight[2] > node.val
                    if not c1 or not c2:
                        return [False, node.val, node.val]
                    
                    maxVal = max(maxVal, fromRight[1])
            
            return [True, maxVal, minVal]

        
        
        if root is None:
            return True
        res = dfs(root)
        
        return res[0]
