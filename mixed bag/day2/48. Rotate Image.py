# first r <-> c
# switch row

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(0, row):
            for c in range(0, col):
                if r < c:
                    temp = matrix[r][c] 
                    matrix[r][c] = matrix[c][r]
                    matrix[c][r] = temp
                    
        for c in range(0, col // 2):
            for r in range(0, row):
                temp = matrix[r][c] 
                matrix[r][c] = matrix[r][col - c - 1]
                matrix[r][col - c - 1] = temp
                                                                
        return
