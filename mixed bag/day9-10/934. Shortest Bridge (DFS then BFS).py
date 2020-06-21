# try 1:  change two island to 1's and 2's, then BFS

class Solution:
    def shortestBridge(self, a: List[List[int]]) -> int:
        
        def dfs(a, r, c):
            
            m, n = len(a), len(a[0])
            
            if a[r][c] == 2:
                return
            
            a[r][c] = 2
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if a[nr][nc] == 1:
                        dfs(a, nr, nc)
            return
        
        m = len(a)
        n = len(a[0])
    
        flip = False
        stack = []
        for r in range(0, m):
            for c in range(0, n):
                if a[r][c] == 1:
                    if flip == False:
                        dfs(a, r, c) # turn to 2's
                        stack.append([r, c])
                        flip = True
                        continue
                if a[r][c] == 2:
                    stack.append([r, c])
                    continue
                
                
        step = 0
        while len(stack) > 0:
            curSize = len(stack)            
            nextStep = []
            for i in range(0, curSize):
                curNode = stack.pop()
                r = curNode[0]
                c = curNode[1]
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n:
                        if a[nr][nc] == 1:
                            return step
                        elif a[nr][nc] == 0:
                            nextStep.append([nr, nc])
                            a[nr][nc] = 2
            
            stack = nextStep
            step += 1
                    
        
        return 0
