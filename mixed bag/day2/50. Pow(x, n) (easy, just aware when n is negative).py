# if n < 0 -> x = 1/x, n = -n
# if n is odd/even


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def rec(x, n, memo):                   
            if n in memo:
                return memo[n]
            else:                
                if abs(n) % 2 == 0:
                    sub = rec(x, n//2, memo)
                    memo[n] = sub * sub                            
                else:
                    sub = rec(x, (n  - 1)//2, memo)                
                    memo[n] = sub * sub * x                
                return memo[n]
        
        
        memo = dict()
        memo[0] = 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        rec(x, n, memo)
        
        return memo[n]
