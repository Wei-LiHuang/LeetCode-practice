class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):            
            
            if node is None:
                return None
            
            fromLeft, fromRight = dfs(node.left), dfs(node.right)
            node.right = fromLeft
            node.left = fromRight
            
            return node
        
        return dfs(root)
                
            
            
            
        
