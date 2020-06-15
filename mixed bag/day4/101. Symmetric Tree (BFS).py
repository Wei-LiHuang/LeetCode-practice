class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        stack = [root]
        
        while len(stack) > 0:            
            curSize = len(stack)            
            nextLevel = []
            for i in range(0, curSize):
                cur = stack.pop()
                if cur is not None:
                    nextLevel.append(cur.left)
                    nextLevel.append(cur.right)
            
            l, r = 0, len(nextLevel) - 1
            while l < r:
                
                if nextLevel[l] is None and nextLevel[r] is None:
                    l += 1
                    r -= 1
                elif nextLevel[l] is None or nextLevel[r] is None:
                    return False
                                    
                elif nextLevel[l].val != nextLevel[r].val:
                    return False
                else:
                    l += 1
                    r -= 1
                
            stack = nextLevel
            
        return True
                
        
