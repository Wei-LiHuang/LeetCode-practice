#boring problem.

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                
        m, n = len(matrix), len(matrix[0])            
        r, c = 0, -1
        path = []        
        while len(path) < (m * n):            
            for d in directions:                
                dr, dc = d[0], d[1]                
                while r + dr >= 0 and r + dr < m and c + dc >= 0 and c + dc < n and matrix[r + dr][c + dc] is not None:                    
                    r, c = r + dr, c + dc
                    path.append(matrix[r][c])
                    matrix[r][c] = None
                    
        return path
        
        
        
