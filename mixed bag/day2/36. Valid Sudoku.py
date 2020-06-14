# only check, not solve

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def dfs(board, rowCheck, colCheck, blockCheck, index) -> bool:
            
            r = index // 9
            c = index % 9
            blockIndex = 3 * (r // 3) + (c // 3)
            
            if index == 81:
                return True
            
            if board[r][c] != ".":
                return dfs(board, rowCheck, colCheck, blockCheck, index + 1)
            
            for i in range(1, 10):                
                if rowCheck[r][i - 1] == 0 and colCheck[c][i - 1] == 0 and blockCheck[blockIndex][i - 1] == 0:
                    board[r][c] = str(i)
                    rowCheck[r][i - 1] = 1
                    colCheck[c][i - 1] = 1
                    blockCheck[blockIndex][i - 1] = 1
                    if dfs(board, rowCheck, colCheck, blockCheck, index + 1):
                        return True
                    board[r][c] = "."
                    rowCheck[r][i - 1] = 0
                    colCheck[c][i - 1] = 0
                    blockCheck[blockIndex][i - 1] = 0
            
            return False
            
                   
        rowCheck, colCheck, blockCheck = [], [], []
        
        #row check        
        for r in range(0, 9):            
            rowCheck.append([0] * 9)
            for c in range(0, 9):
                if board[r][c] != ".":
                    if rowCheck[r][int(board[r][c]) - 1] != 0:
                        return False
                    else:
                        rowCheck[r][int(board[r][c]) - 1] = 1
        #col check        
        for c in range(0, 9):            
            colCheck.append([0] * 9)
            for r in range(0, 9):
                if board[r][c] != ".":
                    if colCheck[c][int(board[r][c]) - 1] != 0:
                        return False
                    colCheck[c][int(board[r][c]) - 1] = 1                
                    
        #blockCheck:                            
        for i in range(0, 9):
            blockCheck.append([0] * 9)
        for r in range(0, 9):            
            for c in range(0, 9):
                if board[r][c] != ".":
                    bIndex = 3 * (r // 3) + (c // 3)
                    if  blockCheck[bIndex][int(board[r][c]) - 1] != 0:
                        return False
                    blockCheck[bIndex][int(board[r][c]) - 1] = 1
                    
                    
        return True
                
