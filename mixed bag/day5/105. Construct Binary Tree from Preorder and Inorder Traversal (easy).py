class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
                
        def rec(Pre, lp, rp, In, li, ri, m):
            
            if lp > rp or li > ri:
                return None
            
            root = TreeNode(Pre[lp], None, None)
            
            # find root in in order:
            
            # speed improve:
            rootI = m[Pre[lp]]
            
            # original:
            #rootI = -1            
            #for i in range(li, ri + 1):
                #if In[i] == Pre[lp]:
                    #rootI = i
                    #break
                    
                    
            # In[li] ~ In[rootI - 1]: left tree
            # size = (rootI - 1 ) - li + 1 => rootI - li
            # x - (lp + 1) + 1 = rootI - li, x = rootI + lp + 1 - 1 - li = rootI + lp - li
            # Pre[lp + 1] ~ Pre[lp + rootI - li]
            
            # original:
            #root.left = rec(Pre, lp + 1, lp + rootI - li, In, li, rootI - 1)
            #root.right = rec(Pre, lp + rootI - li + 1, rp, In, rootI + 1, ri)
            
            # speed improve:
            root.left = rec(Pre, lp + 1, lp + rootI - li, In, li, rootI - 1, m)
            root.right = rec(Pre, lp + rootI - li + 1, rp, In, rootI + 1, ri, m)

            return root
        
        # speed improve:
        m = dict()
        for i in range(0, len(inorder)):
            m[inorder[i]] = i
        
        return rec(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, m)
            
