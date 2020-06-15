class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        
        m = len(b)
        n = len(b[0])
                
        def dfs (b, word, curIndex, index):
                                    
            r = index // n
            c = index % n
            
            if curIndex == len(word) - 1 and b[r][c] == word[curIndex]:                
                return True
            
            char = b[r][c]
            b[r][c] = None                                                 
            
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]            
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]                    
                if nr >= 0 and nr < m and nc >= 0 and nc < n and b[nr][nc] == word[curIndex + 1]:
                    if dfs(b, word, curIndex + 1, nr * n + nc):
                        return True
                        
            b[r][c] = char
            return False
                        
                
        for r in range(0, m):
            for c in range(0 , n):            
                if b[r][c] == word[0]:
                    if dfs(b, word, 0, r * n + c):
                        return True                    
                    
                    
        return False
                    
