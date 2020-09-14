# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        
        def getTotalSum(cur, _sum):            
            _sum[0] += cur.val            
            if cur.left is not None:
                getTotalSum(cur.left, _sum)
            if cur.right is not None:
                getTotalSum(cur.right, _sum)
            return
        
        def findMaxProduct(cur, totalSum, res):
                        
            sumFromLeftTree, sumFromRightTree = 0, 0
            
            if cur.left is not None:
                sumFromLeftTree = findMaxProduct(cur.left, totalSum, res)
                
            if cur.right is not None:
                sumFromRightTree = findMaxProduct(cur.right, totalSum, res)
                
            curSum = cur.val + sumFromLeftTree + sumFromRightTree
            product = ((totalSum - curSum) * curSum)                  
            if product  > res[0]:
                res[0] = product
                
            return curSum
                
        _sum = [0]
        getTotalSum(root, _sum)
        
        res = [0]
        findMaxProduct(root, _sum[0], res)
        
        return res[0] % (10**9 + 7)      
                
