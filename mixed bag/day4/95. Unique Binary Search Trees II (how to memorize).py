class Solution:
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def rec(l, r):
            
            if l == r:
                return [TreeNode(l)]
            
            if l == r - 1:                
                n1 = TreeNode(l, None, None)
                n1.right = TreeNode(r, None, None)
                
                n2 = TreeNode(r, None, None)
                n2.left = TreeNode(l, None, None)                
                return [n1, n2]
            
            res = []            
            for i in range(l, r + 1):                
                leftSubTree, rightSubTree = None, None
                if i == l:
                    rightSubTree = rec(l + 1, r)
                    leftSubTree = [None]                    
                elif i == r:
                    leftSubTree = rec(l, r - 1)                    
                    rightSubTree = [None]
                else:
                    leftSubTree = rec(l, i - 1)
                    rightSubTree = rec(i + 1, r)
                    
                for ln in leftSubTree:
                    for rn in rightSubTree:
                        subRoot = TreeNode(i, None, None)
                        subRoot.left = ln
                        subRoot.right = rn
                        res.append(subRoot)
                        
            return res
        
        if n == 0:
            return None
        
        return rec(1, n)
                
