# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        
        def dfs(cur):
            
            if cur.left is None and cur.right is None:
                return [cur, cur]
                        
            lNode = cur.left
            rNode = cur.right
            
            cur.left = None
            cur.right = None
            
            if lNode is not None:                
                fromLeft = dfs(lNode)                                                                
                cur.right = fromLeft[0]
                
                if rNode is not None:
                    fromRight = dfs(rNode)
                    fromLeft[1].right = fromRight[0]                    
                    return [cur, fromRight[1]]                
                else:
                    return [cur, fromLeft[1]]
                
            else:
                fromRight = dfs(rNode)
                cur.right = fromRight[0]
                return [cur, fromRight[1]]
            
        
        if root is None:
            return None
        
        return dfs(root)
                
                
            
            
