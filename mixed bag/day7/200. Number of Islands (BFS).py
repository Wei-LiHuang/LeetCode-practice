class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def getNeighbors(grid, index, visited):
            if index in visited:
                return []
            visited.add(index)
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]            
            neighbors = []
            for d in directions:
                nr = (index // n) + d[0]
                nc = (index % n) + d[1]       
                nIndex = nr * len(grid[0]) + nc
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == "1" and nIndex not in visited:
                    neighbors.append(nIndex)
                    
            return neighbors
                            
        m = len(grid)
        if m == 0:
            return 0        
        n = len(grid[0])
        if n == 0:
            return 0
        
        count = 0
        visited = set()
        for i in range(0, m * n):            
            if i in visited:                
                continue            
            r = i // n
            c = i % n            
            if grid[r][c] == "1":
                count += 1
                stack = [i]
                while len(stack) > 0:
                    curSize = len(stack)
                    neighbors = []
                    for j in range(0, curSize):
                        curNode = stack.pop()
                        neighbors.extend(getNeighbors(grid, curNode, visited))
                    stack = neighbors
        
        return count
