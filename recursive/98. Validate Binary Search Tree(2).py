class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        def dfs(node, parentVal, isLeft, isRight):
                        
            # if is a leaf node:
            # is left: smaller than parent return [result: bool, min: left, max: left]
            # is right: bigger than parent, return [result: bool, min: right, max: right]
            if not node.left and not node.right:
                if isLeft and node.val < parentVal:
                    return [True, node.val, node.val]
                elif isRight and node.val > parentVal:
                    return [True, node.val, node.val]
                else:
                    return [False, None, None]
                
            if (isLeft and node.val > parentVal) or (isRight and node.val < parentVal):
                return [False, None, None]
            
            # if is a one sided node:
            # not right: fromRight = [True, node.val, node.val]
            # not left: fromLeft = [True, node.val, node.val]
            
            # if is a full node:
            # fromLeft must be true, and result[2] must smaller than node.val
            # fromRight must be true, and result[1] must bigger than node.val
            fromLeft, fromRight = [True, node.val, node.val], [True, node.val, node.val]
            if node.left:
                fromLeft = dfs(node.left, node.val, True, False)
                if not fromLeft[0] or node.val <= fromLeft[2]:
                    return [False, None, None]
                                                    
            if node.right:
                fromRight = dfs(node.right, node.val, False, True)
                if not fromRight[0] or node.val >= fromRight[1]:
                    return [False, None, None]
                                
            # return [True, fromLeft.min, fromRight.max]
            return [True, fromLeft[1], fromRight[2]]
            
        
        if not root or (not root.left and not root.right):
            return True
        
        res = dfs(root, None, False, False )
        
        return res[0]

            
                
            
