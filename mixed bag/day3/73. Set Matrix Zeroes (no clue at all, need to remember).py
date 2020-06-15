# no clue at all
# need to remember

class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        m, n = len(a), len(a[0])        
        
        # 1. check first row:
        needToTurnFirstRow = False
        for i in range(0, n):
            if a[0][i] == 0:
                needToTurnFirstRow = True
                break
                
        # 2. check first col:
        needToTurnFirstCol = False
        for i in range(0, m):
            if a[i][0] == 0:
                needToTurnFirstCol = True
                break
                
        # 3. check other row and col:        
        for i in range(0, m):            
            for j in range(0, n):
                if a[i][j] == 0:
                    a[i][0] = 0
                    a[0][j] = 0
                    
        # 4. turn all row from row 1:        
        for i in range(1, m):
            if a[i][0] == 0:
                for j in range(1, n):
                    a[i][j] = 0
        
        # 4. turn all col from col 1:        
        for i in range(1, n):
            if a[0][i] == 0:
                for j in range(1, m):
                    a[j][i] = 0        
                    
        # 5. turn first row:
        if needToTurnFirstRow:
            for i in range(0, n):
                a[0][i] = 0
        
        # 6. turn first col:
        if needToTurnFirstCol:
            for i in range(0, m):
                a[i][0] = 0
                    
        return
