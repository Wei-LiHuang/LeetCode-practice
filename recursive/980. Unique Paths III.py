class Solution:
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c, grid, path, targetLength, res):
            
            n = len(grid[0])
            index = (r * n + c)
            
            if index in path:
                return
            
            if grid[r][c] == -1:
                return
            
            path.add(index)            
            
            if grid[r][c] == 2 and len(path) == targetLength:
                res[0] += 1
                path.remove(index)
                return
                        
            if r > 0:
                dfs(r - 1, c, grid, path, targetLength, res)
            
            if r < len(grid) - 1:
                dfs(r + 1, c, grid, path, targetLength, res)
                
            if c > 0:
                dfs(r, c - 1, grid, path, targetLength, res)
            
            if c < n - 1:
                dfs(r, c + 1, grid, path, targetLength, res)
                
            path.remove(index)
            
            return
                                
        m, n, res = len(grid), len(grid[0]), [0]
                
        sr, sc = -1, -1
        targetLength = 0
        for r in range(0, m):
            for c in range(0, n):
                if grid[r][c] != -1:
                    targetLength += 1
                if grid[r][c] == 1:
                    sr, sc = r, c
                
        path = set()
        dfs(sr, sc, grid, path, targetLength, res)
        
        return res[0]
