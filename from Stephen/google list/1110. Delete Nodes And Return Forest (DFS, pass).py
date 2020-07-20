# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(curNode, toDel, res):
            
            if curNode.left is not None:
                curNode.left = dfs(curNode.left, toDel, res)
            
            if curNode.right is not None:
                curNode.right = dfs(curNode.right, toDel, res)
                
            if curNode.val in toDel:
                if curNode.left is not None:
                    res.append(curNode.left)
                if curNode.right is not None:
                    res.append(curNode.right)                    
                return None
            
            return curNode
                                
        toDel = set()
        for td in to_delete:
            toDel.add(td)
                
        res = []
        dummy = TreeNode(-1, root, None)
        toDel.add(-1)
        
        dfs(dummy, toDel, res)
        
        return res
