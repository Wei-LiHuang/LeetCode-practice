# dfs(node) return [node has cam, node has no cam and not satisfied, node has no cam but satisfied]

class Solution:
        
    def minCameraCover(self, root: TreeNode) -> int:
        
        def dfs(node):
            
            inf = float('inf')
            
            if node is None:
                return [0, 0, inf]
            
            r = dfs(node.right)
            l = dfs(node.left)
            
            if node.left is None and node.right is None:
                # leaf node
                return [1, 0, inf]
            
            elif node.left is None and node.right is not None:
                return [1 + min(r), r[2], r[0]]
                                
            elif node.left is not None and node.right is None:                
                return [1 + min(l), l[2], l[0]]
                                
            elif node.left is not None and node.right is not None:                                        
                x = 1 + min(l) + min(r)                
                y = l[2] + r[2]
                z = min([r[0] + l[0], r[0] + l[2], l[0] + r[2]])                                    
                return [x, y, z]
                                                                        
                                                                        
        res = dfs(root)        
        return min(res[0], res[2])
