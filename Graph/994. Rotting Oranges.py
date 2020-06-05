class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # scan for rotten oranges and fresh oranges
        # start to do bfs for all rotten oranges, removing fresh oranges from the fresh set
        # if the bfs ends and no fresh oranges left -> return minutes, else return -1
        # --> wrong result: [[2],[1],[1],[1],[2],[1],[1]]
        
        # check each fresh -> rotten, when zero fresh, return minutes. if no more fresh become rottec, return -1
        
        
        def willRot(grid, curR, curC, rottenOranges): #O(1)
            m = len(grid)
            n = len(grid[0])
            
            #up:
            upIndex = (curR - 1) * n + curC
            if curR > 0 and upIndex in rottenOranges:
                return True         
            #down:
            downIndex = (curR + 1) * n + curC
            if curR < m - 1 and downIndex in rottenOranges:
                return True                   
            #left:
            leftIndex = (curR) * n + curC - 1
            if curC > 0 and leftIndex in rottenOranges:
                return True                           
            #right
            rightIndex = (curR) * n + curC + 1
            if curC < n - 1 and rightIndex in rottenOranges:
                return True
                
            return False
        
        m = len(grid)
        if m == 0:
            return 0
        
        n = len(grid[0])
        if n == 0:
            return 0
        
        #O(m * n)
        rottenOranges, freshOranges = set(), set()
        for r in range(0, m):
            for c in range(0, n):
                if grid[r][c] == 1:
                    freshOranges.add(r * n + c)
                if grid[r][c] == 2:
                    rottenOranges.add(r * n + c)
                    
        if len(freshOranges) == 0:
            return 0
                                    
        stack = list(freshOranges)
        minutes = 1
        
        # O(freshCount0 * freshCount0), freshCount0 <= m * n = N -> O(N^2)
        while len(stack) > 0: 
            # if we have freshCount0 fresh, and each minutes will remove one fresh orange -> O(freshCount0)
            stillFresh = []
            change = []
            curSize = len(stack)
            for i in range(0, curSize): #O(freshCount0)
                curO = stack[i]
                if willRot(grid, curO // n, curO % n, rottenOranges):
                    change.append(curO)
                else:
                    stillFresh.append(curO)
            
            for c in change: #O(changeCount0) <= O(freshCount0)
                rottenOranges.add(c)
                freshOranges.remove(c)
                
            if len(freshOranges) == 0:
                return minutes
            
            minutes += 1
            if len(stillFresh) == len(stack):
                return -1
            else:
                stack = stillFresh
        
        return -1
