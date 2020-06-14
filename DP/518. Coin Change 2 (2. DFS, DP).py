class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:
        
        def DFS(amount, coins):
            def dfs(curAmount, RightMostCoinIndex, tgt, coins, memo):

                if memo[curAmount][RightMostCoinIndex] is not None:
                    return memo[curAmount][RightMostCoinIndex]

                if curAmount == tgt:
                    memo[curAmount][RightMostCoinIndex] = 1                
                    return 1

                res = 0
                for i in range(RightMostCoinIndex, -1, -1):
                    useCoin = coins[i]
                    if curAmount + useCoin <= tgt:
                        res += dfs(curAmount + useCoin, i, tgt, coins, memo)

                memo[curAmount][RightMostCoinIndex] = res            
                return res

            if amount == 0:
                return 1

            n = len(coins)
            if n == 0:
                return 0

            memo = []
            for i in range(0, amount + 1):
                memo.append([None] * n)
                                        
            return dfs(0, n - 1, amount, coins, memo)
        
        
        def DP(amount, coins):
            
            n = len(coins)
            dp = [0] * (amount + 1)
            dp[0] = 1
            
            for c in coins:
                for curAmount in range(1, amount + 1):
                    if curAmount - c >= 0:
                        dp[curAmount] = dp[curAmount - c] + dp[curAmount]
            
            return dp[amount]
                
                
                                                                                                                            
        return DP(amount, coins)
            
                
            
        
        
