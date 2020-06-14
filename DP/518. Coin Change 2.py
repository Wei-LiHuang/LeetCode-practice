#dp[val] = (只用 c0 去組合能有幾種) + (只用 c0, c1去組合能有幾種) + ... + (用 c0, c1, c2, c3 ... ci - 1 去組合能有幾種)
#(只用 c0 去組合能有幾種) 和 只用 (c0, c1去組合能有幾種) 的關係?
class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1) # 0 ~ amount
        dp[0] = 1 # 一種組合:空集合
        
        for i in range(0, len(coins)):                        
            #用c0, c1, c2, ..., ci 硬幣,組合能有幾種?            
            for val in range(1, amount + 1):                
                tgt = val - coins[i]
                if tgt >= 0:                    
                    dp[val] += dp[tgt]
        
        return dp[amount]
