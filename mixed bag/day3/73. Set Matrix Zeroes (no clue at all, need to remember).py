class Solution:
    
    def setZeroes(self, a: List[List[int]]) -> None:
        m = len(a)
        n = len(a[0])
        
        #first check first row:
        firstRowNeedFlip = False        
        for i in range(0, n):
            if a[0][i] == 0:
                firstRowNeedFlip = True
                break
        # first col check:
        firstColNeedFlip = False        
        for i in range(0, m):
            if a[i][0] == 0:
                firstColNeedFlip = True
                break
        
        # record on the first col and first row:
        for i in range(1, m):
            for j in range(1, n):                
                if a[i][j] == 0:
                    a[0][j] = 0
                    a[i][0] = 0
                    
        # flip rows:
        for i in range(1, m):
            if a[i][0] == 0:            
                for j in range(1, n):
                    a[i][j] = 0
        #flip cols:
        for j in range(1, n):
            if a[0][j] == 0:            
                for i in range(1, m):
                    a[i][j] = 0
                    
        if firstRowNeedFlip:
            for j in range(0, n):
                a[0][j] = 0
                
        if firstColNeedFlip:
            for i in range(0, m):
                a[i][0] = 0
        
        return
