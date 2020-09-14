class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        
        directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        
        dp = []
        for i in range(0, n):
            dp.append([0] * n)
            
        dp[r][c] = 1
        for step in range(0, k):
            dp2 = []
            for i in range(0, n):
                dp2.append([0] * n)
                
            for r in range(0, n):
                for c in range(0, n):
                    if dp[r][c] > 0:
                        for d in directions:
                            nr, nc = r + d[0], c + d[1]
                            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                                dp2[nr][nc] += dp[r][c]/8
            dp = dp2
            
        res = 0
        for row in dp:
            res += sum(row)
        
        return res
            
                                        
    def knightProbability_TLE(self, N: int, K: int, r: int, c: int) -> float:
        '''
            prob of staying in board = 1 - (prob of out of board before k moves)
            
            let P = the prob of out of board after k moves
            
            P =   prob of out of board after 0 move (always 0)
                + prob of out of board after 1 move
                + prob of out of board after 2 moves
                + ...
                + prob of out of board after k moves
                
            P = p[1] + p[2] +  ... + p[k], where p[i] = prob of out of board after i moves
            
            p[0] = 0
            p[1] = if there are x moves that will be out of board, p[1] = x / 8
            p[2] = (1 - p[1]) * (y / 8)
            p[3] = (1 - p[1] - p[2]) * (z / 8)
            ...
            p[k] = (1 - p[1] - p[2] - ... - p[k - 1]) * (? / 8)
            
            -> res = 1 - (p[1] + p[2] + ... + p[k])                                
            
            if we have a table for each pos (x, y), how many from the 8 choices will be out of board -> spped up            
        '''        
        def checkOutOfBoard(n, r, c, d):            
            index = r * n + c
            if index in d:
                return d[index]
            
            directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
            
            res = []
            count = 0
            for _dir in directions:
                nr, nc = r + _dir[0], c + _dir[1]
                if nr >= 0 and nr < n and nc >= 0 and nc < n:
                    res.append([nr, nc])
            d[index] = res
            return d[index]
                        
        d = dict()                                            
        _sumP = [1] * (K + 1)
        _sumP[0] = 0
        
        q = collections.deque()
        q.append([r, c])
        step = 0        
        while len(q) > 0 and step < K:
            curSize = len(q)
            step += 1     
            
            allNext = curSize * 8
            stillIn = 0
            
            for i in range(0, curSize):
                popped = q.pop()
                r, c = popped[0], popped[1]
                stillInBoard = checkOutOfBoard(N, r, c, d)
                for _next in stillInBoard:
                    q.appendleft(_next)
                stillIn += len(stillInBoard)
                
            outProb = (1 - _sumP[step - 1]) * ((allNext - stillIn) / allNext)
            _sumP[step] = outProb + _sumP[step - 1]
        
        return 1 - _sumP[K]
            

            
            
        
        
