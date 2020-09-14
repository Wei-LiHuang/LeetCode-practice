class Solution:
    def numSubmat(self, a: List[List[int]]) -> int:
        
        '''
            1 0 1
            1 1 0
            1 1 0
            
            -> row0 ~ row0 -> col0 ~ col2 -> 1 x 1: 2
            -> row0 ~ row1 -> col0 ~ col2 -> 1 x 2: 1
            -> row0 ~ row2 -> col0 ~ col2 -> 1 x 3: 1
            -> row1 ~ row1 -> col0 ~ col2 -> 1 x 1: 2
            -> row1 ~ row2 -> col0 ~ col2 -> 1 x 2: 2, 2 x 1: 2, 2 x 2 = 1
            -> row2 ~ row2 -> col0 ~ col2 -> 1 x 1: 2
            
            2 + 1 + 1 + 2 + 2 + 2 + 1 + 2
                = 13                                
        '''
        m = len(a)
        n = len(a[0])
        
        def oneDHelper(A):
            res = 0
            l = 0
            for i in range(0, len(A)):
                if A[i] == 0:
                    l = 0        
                else:
                    l = l + 1        
                res += l                
            return res

        count = 0
        for r1 in range(0, m):            
            isAll1 = a[r1]            
            for r2 in range(r1, m):
                
                for c in range(0, n):
                    if a[r2][c] == 0:
                        isAll1[c] = 0
                
                count += oneDHelper(isAll1)
                                                
        return count
                
                
                    
                    
                    
