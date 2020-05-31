class Solution:
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def dfs(node: TreeNode, val: int):
            if not node:                
                return TreeNode(val)
            
            if not node.left and not node.right:                                                
                if node.val < val:
                    node.right = TreeNode(val)                    
                else:
                    node.left = TreeNode(val)
                return node
                    
            if node.val < val:
                if node.right:
                    dfs(node.right, val)
                else:
                    node.right = TreeNode(val)
                return node
            
            else:
                if node.left:
                    dfs(node.left, val)                    
                else:
                    node.left = TreeNode(val)
                return node
            
        return dfs(root, val)
