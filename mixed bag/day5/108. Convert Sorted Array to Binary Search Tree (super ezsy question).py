class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def creatTree(a, l, r):
            
            if l > r:
                return None
            
            if l == r:
                return TreeNode(a[l])
            
            if l == r - 1:
                n1 = TreeNode(a[l])
                n2 = TreeNode(a[r])
                n1.right = n2
                return n1
            
            mid = (l + r) // 2
            
            node = TreeNode(a[mid])
            
            node.left = creatTree(a, l, mid - 1)
            node.right = creatTree(a, mid + 1, r)
            
            return node
        
        
        return creatTree(nums, 0, len(nums) - 1)
