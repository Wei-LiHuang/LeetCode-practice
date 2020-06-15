class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        
        def dfs(node, count, res):
            
            if node.left is None and node.right is None:
                res[0] = max(res[0], count)
            
            if node.left is not None:
                dfs(node.left, count + 1, res)
            
            if node.right is not None:
                dfs(node.right, count + 1, res)
                
            return
        
        if root is None:
            return 0
        
        res = [0]
        dfs(root, 1, res)
        return res[0]
