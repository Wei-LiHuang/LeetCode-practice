class Solution:
    
    def exist(self, b: List[List[str]], word: str):
        
        def dfs(r, c, word, index, b):
            
            m, n = len(b), len(b[0])
            
            if index == len(word) - 1:
                return True
            
            temp = b[r][c]
            b[r][c] = None
                        
            directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]            
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]                
                if nr >= 0 and nr < m and nc >= 0 and nc < n:                    
                    if b[nr][nc] == word[index + 1]:                        
                        if dfs(nr, nc, word, index + 1, b):
                            return True
                        
            b[r][c] = temp            
            return False
        
        m, n = len(b), len(b[0])
        
        for r in range(0, m):
            for c in range(0, n):
                if b[r][c] == word[0]:                    
                    if dfs(r, c, word, 0, b):
                        return True
        return False
