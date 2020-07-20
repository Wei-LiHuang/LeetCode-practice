class Solution:
    
    def stoneGameII(self, a: List[int]) -> int:
        
        '''
            from: https://www.youtube.com/watch?v=e_FrC5xavwI
            solve(i, m):
             return the maximum score a player can get when:
                 1. the piles = [a[i], a[i + 1], ..., a[n - 1]]
                 2. a player can take X = (1 to 2 * m) stones
                 3. after taking X stone, the next player will take solve(i + X, max(m, X)) score        
        '''                        
        def solve(a, i, m, memo):            
            n = len(a)
            
            if memo[i][m] is not None:
                return memo[i][m]            
            
            if i + 2 * m >= n:
                memo[i][m] = sum(a[i:n])
                return memo[i][m]
            
            # we want to take X piles to make the next player get the min score in the next turn:
            maxDis = min((n - 1) - i + 1, 2 * m + 1)
            nextPlayerMinScore = float('inf')
            for x in range(1, maxDis):
                nextPlayerMinScore = min(nextPlayerMinScore, solve(a, i + x, max(m, x), memo))
                        
            memo[i][m] = sum(a[i : n]) - nextPlayerMinScore
            
            #print([i, m, memo[i][m]])
            
            return memo[i][m] 
                                                                    
        n = len(a)
        memo = []
        for i in range(0, n):
            # max possible m = len(a), which means taking all the stones
            memo.append([None] * (n + 1)) 
        
                        
        # maximum score a player can get starting from a0 and m = 1
        solve(a, 0, 1, memo)
        #return solve(a, 0, 1, memo)
        print(memo)
        return memo[0][1]
