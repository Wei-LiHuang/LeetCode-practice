class Solution:
    
    def solve(self, b: List[List[str]]) -> None:
        
        def dfs(index, b , visited, stays):
            
            m, n = len(b), len(b[0])
            
            visited.add(index)
            stays.add(index)
            
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            r, c = index // n, index % n
            
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                nIndex = nr * n + nc
                if nr >= 0 and nr < m and nc >= 0 and nc < n and b[nr][nc] == "O" and (nIndex) not in visited:
                    dfs(nIndex, b, visited, stays)
            return
            
            
        
        m = len(b)
        if m == 0:
            return b
        
        n = len(b[0])
        
        stays, visited = set(), set()        
        
        for c in range(0, n):            
            index = c
            if b[0][c] == "O":
                dfs(index, b, visited, stays)
                
        for c in range(0, n):            
            index = (m - 1) * n + c
            if b[m - 1][c] == "O":
                dfs(index, b, visited, stays)
        
        for r in range(0, m):            
            index = r * n + 0
            if b[r][0] == "O":
                dfs(index, b, visited, stays)
                
        for r in range(0, m):            
            index = r * n + n - 1
            if b[r][n - 1] == "O":
                dfs(index, b, visited, stays)
                
        for i in range(0, m * n):
            r = i // n
            c = i % n
            if b[r][c] == "O" and i not in stays:
                b[r][c] = "X"
        
        return
