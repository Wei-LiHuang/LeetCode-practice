# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        res, stack = 1, [[0, root]] # root
        
        while len(stack) > 0:
            nextLevel = []
            left, right = float('inf'), -float('inf')
            size = len(stack)
            for i in range(0, size):
                cur = stack.pop()
                index = cur[0]
                left = min(left, index)
                right = max(right, index)
                node = cur[1]
                if node.left:
                    nextLevel.append([2 * index + 1, node.left])
                if node.right:
                    nextLevel.append([2 * index + 2, node.right])
            
            res = max(res, right - left + 1)
            stack = nextLevel
        
                                                                    
        return res
