class Solution:
    
    def sumNumbers(self, root: TreeNode) -> int:
        
        def dfs(cur, path, res):
            
            if cur.left is None and cur.right is None:                                
                path.append(cur.val)                
                val, mul = 0, 1
                for i in range(len(path) - 1, -1, -1):
                    val += (path[i] * mul)
                    mul *= 10                    
                res[0] += val
                path.pop()
                return
            
            path.append(cur.val)
            if cur.left is not None:
                dfs(cur.left, path, res)
            if cur.right is not None:
                dfs(cur.right, path, res)                                        
            path.pop()
            
            return
        
        if root is None:
            return 0
        
        res = [0]
        dfs(root, [], res)
        
        return res[0]
            
            
        
