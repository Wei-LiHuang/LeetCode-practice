class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        '''
            answer[i][j] is 
            the sum of all elements mat[r][c] 
            for i - K <= r <= i + K, 
                j - K <= c <= j + K, 
            
            and (r, c) is a valid position in the matrix.                                
            -> a[i][j] = sum from row1: i - k, col1: j - k, row2: i + k, col2: j + k                        
        '''
        m = len(mat)        
        n = len(mat[0])
        ans, d = [], []
        for i in range(0, m + 1):
            d.append([0] * (n + 1))
        
        for i in range(0, m):
            ans.append([0] * n)
        
        for i in range(0, m):
            for j in range(0, n):
                d[i + 1][j + 1] = d[i][j + 1] + d[i + 1][j] + mat[i][j] - d[i][j]
                
    
        for i in range(0, m):
            for j in range(0, n):
                r1, r2, c1, c2 = max(0, i - k), min(m - 1, i + k), max(0, j - k), min(n - 1, j + k)                
                ans[i][j] = d[r2 + 1][c2 + 1] - d[r1][c2 + 1] - d[r2 + 1][c1] + d[r1][c1]
        
        return ans
        
        
