class Solution:
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def dfs(val, node):
            
            if node is None:
                return TreeNode(val)
            
            if node.left is None and node.right is None:
                if node.val > val:
                    node.left = TreeNode(val)
                else:
                    node.right = TreeNode(val)
                return node
            
            if node.val > val:
                node.left = dfs(val, node.left)
            else:
                node.right = dfs(val, node.right)
            
            return node
        
        return dfs(val, root)
