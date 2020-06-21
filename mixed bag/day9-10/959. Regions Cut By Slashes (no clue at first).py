# no clue at first, need to remember this slash to new grid
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
                
        def dfs(a, r, c, visited, color):
            n = len(a)
            index = r * n + c
            if index in visited:
                return            
            visited.add(index)            
            a[r][c] = color
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]            
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if nr >= 0 and nr < n and nc >= 0 and nc < n:
                    if (nr * n + nc) not in visited and a[nr][nc] != -1:
                        dfs(a, nr, nc, visited, color)                                                            
            return
                                                                    
        n = len(grid)        
        
        # build 9 * N * N gird
        a = []        
        row, odd, even = 0, 1, 2
        # O(N^2)
        for i in range(0, n):
            
            row += 3
            a.append([])
            a.append([])
            a.append([])
            
            for j in range(0, n):
                
                if grid[i][j] == ' ':
                    a[row - 3].extend([0, 0, 0])
                    a[row - 2].extend([0, 0, 0])
                    a[row - 1].extend([0, 0, 0])
                    
                elif grid[i][j] == '/':
                    a[row - 3].extend([odd, odd, -1])
                    a[row - 2].extend([odd, -1, even])
                    a[row - 1].extend([-1, even, even])                    
                    odd += 2
                    even += 2
                
                elif grid[i][j] == '\\':
                    a[row - 3].extend([-1, odd, odd])
                    a[row - 2].extend([even, -1, odd])
                    a[row - 1].extend([even, even, -1])                    
                    odd += 2
                    even += 2
                
        # color each grid:        
        m, colored = len(a), set()
        for r in range(0, m):
            for c in range(0, m):
                if a[r][c] != 0 and a[r][c] != -1:
                    _color = a[r][c]
                    if _color not in colored:
                        dfs(a, r, c, set(), _color)
                        colored.add(_color)
                                                        
        return len(colored)
