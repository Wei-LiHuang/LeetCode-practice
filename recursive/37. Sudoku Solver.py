class Solution:
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        
        def dfs(rowCheck, colCheck, blockCheck, b, i):                                
            
            if i == 81:
                return True
            
            r, c = int(i / 9), int(i % 9)
            block = int(r / 3) * 3 + int(c / 3)
            
            solved = False
            if b[r][c] == ".":            
                for val in range(1, 10):
                    if rowCheck[r][val - 1] != 1 and colCheck[c][val - 1] != 1 and blockCheck[block][val - 1] != 1:
                        b[r][c] = str(val)
                        rowCheck[r][val - 1], colCheck[c][val - 1], blockCheck[block][val - 1]  = 1, 1, 1
                        if dfs(rowCheck, colCheck, blockCheck, b, i + 1):
                            solved = True
                            break
                        else:
                            b[r][c] = "."
                            rowCheck[r][val - 1], colCheck[c][val - 1], blockCheck[block][val - 1]  = 0, 0, 0
            else:
                return dfs(rowCheck, colCheck, blockCheck, b, i + 1)
                
            return solved
                                
        #row checker:
        rowCheck = []
        for i in range(0, 9):
            row = [0] * 9
            for j in range(0, 9):
                if board[i][j] != '.':
                    row[int(board[i][j]) - 1] = 1
                
            rowCheck.append(row)
            
        #col checker:
        colCheck = []
        for j in range(0, 9):
            col = [0] * 9
            for i in range(0, 9):
                if board[i][j] != '.':
                    col[int(board[i][j]) - 1] = 1
                
            colCheck.append(col)            
            
        #block checker:
        blockCheck = []
        for i in range(0, 9):
            blockCheck.append([0] * 9)
        for i in range(0, 9):            
            for j in range(0, 9):
                if board[i][j] != '.':
                    blockR = int(i / 3)
                    blockC = int(j / 3)
                    block = blockR * 3 + blockC
                    blockCheck[block][int(board[i][j]) - 1] = 1
        
        #dfs
        dfs(rowCheck, colCheck, blockCheck, board, 0)
                    
                    
        return

        
                
                
