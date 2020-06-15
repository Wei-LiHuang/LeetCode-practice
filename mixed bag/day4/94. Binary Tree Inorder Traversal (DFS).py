class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def inorder(node, path):
            
            if node.left is None and node.right is None:
                path.append(node.val)
                return
                        
            if node.left is not None:
                inorder(node.left, path)
                
            path.append(node.val)
                
            if node.right is not None:
                inorder(node.right, path)
                
            return
        
        if root is None:
            return []
        
        path = []
        inorder(root, path)
        return path
