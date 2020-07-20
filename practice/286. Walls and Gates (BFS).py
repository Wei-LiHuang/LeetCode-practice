class Solution:
    def wallsAndGates(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """        
        
        if len(a) == 0:
            return 
        
        m, n = len(a), len(a[0])
        inf = 2147483647
        
        q = collections.deque()
        for i in range(0, m):
            for j in range(0, n):
                if a[i][j] == 0:
                    q.append([i, j])
                            
        while len(q) > 0:
            curSize = len(q)
            for i in range(0, curSize):
                curNode = q.pop()                
                r, c = curNode[0], curNode[1]
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n:
                        if a[nr][nc] == inf:
                            a[nr][nc] = a[r][c] + 1
                            q.appendleft([nr, nc])                                                                        
        return
                
