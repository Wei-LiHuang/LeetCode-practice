class Solution:
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        '''
            W: w[i], w[i + 1], ..., w[m - 1]
            B: b[j], b[j + 1], ..., b[n - 1]
        
                minDis = min( Dis(w[i], b[k]) + min(W[i + 1:n], B[j:k] + B[k + 1:n]) )                
                1. calculate the distance between each worker and every bikes
                2. starting from the last worker: w[m - 1], when he picks bikes from b[0] ~ b[n - 1]
                   the next worker w[m - 2] can pick another bike ....
                   get every combination and return the min one
                   
                3. from discuss: how to memoization?
                    
        '''
        
        def rec(workers, bikes, curWorker, bikesLeft, memo):
            
            info = (curWorker, tuple(bikesLeft))
            if info in memo:
                return memo[info]
            
            if curWorker == len(workers):
                return 0
            
            res = float('inf')
            for i in range(0, len(bikesLeft)):
                if bikesLeft[i] == True:
                    bikesLeft[i] = False
                    wx, wy = workers[curWorker][0], workers[curWorker][1]
                    bx, by = bikes[i][0], bikes[i][1]
                    m_dis = abs(wx - bx) + abs(wy - by)
                    res = min(res, m_dis + rec(workers, bikes, curWorker + 1, bikesLeft, memo))
                    bikesLeft[i] = True
            
            memo[info] = res
            return memo[info]
        
        
        memo = dict()
        bikesLeft = [True] * len(bikes)
        
        return rec(workers, bikes, 0, bikesLeft, memo)
