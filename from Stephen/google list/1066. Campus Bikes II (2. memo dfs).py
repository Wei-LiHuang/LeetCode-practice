class Solution:
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        '''
            we have N workers and M bikes.
            for w[n - 1], he takes b[m - 1], b[m - 2], b[m - 3], ..., b[0]
            for w[n - 2], he takes b[m - 1], b[m - 2], b[m - 3], ..., b[0], except the bike w[n - 1] took away                        
        '''
        
        def rec(workers, bikes, availible, dp, worker):
            
            if worker >= len(workers):
                return 0
            
            t = tuple(availible)
            if t in dp[worker]:
                return dp[worker][t]
            
            minDis = float('inf')
            for i in range(0, len(bikes)):
                if availible[i] == True:
                    dis = abs(workers[worker][0] - bikes[i][0]) + abs(workers[worker][1] - bikes[i][1])
                    availible[i] = False
                    minDis = min(minDis, dis + rec(workers, bikes, availible, dp, worker + 1))
                    availible[i] = True
            
            dp[worker][t] = minDis
            return minDis
                                                                            
        N = len(workers)
        M = len(bikes)        
        availible = [True] * M
        dp = dict()
        for i in range(0, N):
            dp[i] = dict()
            
        return rec(workers, bikes, availible, dp, 0)
