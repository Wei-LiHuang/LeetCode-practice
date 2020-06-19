# DP, O(n^2), then think of O(n) -> TLE
# DP, O(2n) , passed --> if a[i] >0, ==0, <0, what's the relation with res[i + 1]?

class Solution:
    
    def maxProduct(self, a: List[int]) -> int:    
        n, _max = len(a), -float('inf')
        dpPos, dpNeg = [None] * n, [None] * n
        
        for i in range(n - 1, -1, -1):            
            if i == n - 1:
                if a[i] > 0:
                    dpPos[i] = a[i]
                    dpNeg[i] = None
                elif a[i] < 0:
                    dpPos[i] = None
                    dpNeg[i] = a[i]
            else:        
                if a[i] > 0:
                    if dpPos[i + 1] is None:
                        dpPos[i] = a[i]
                    else:
                        dpPos[i] = a[i] * dpPos[i + 1]
                    
                    if dpNeg[i + 1] is None:
                        dpNeg[i] = None
                    else:
                        dpNeg[i] = a[i] * dpNeg[i + 1]                                                                                         
                elif a[i] < 0:
                    if dpNeg[i + 1] is None:
                        dpNeg[i] = a[i]
                    else:
                        dpPos[i] = a[i] * dpNeg[i + 1]
                    
                    if dpPos[i + 1] is None:
                        dpNeg[i] = a[i]
                    else:
                        dpNeg[i] =  a[i] * dpPos[i + 1]
                                                                            
            _max = max(_max, a[i])
            if dpPos[i] is not None:
                _max = max(_max, dpPos[i])
            
        return _max
                                                                        
    def maxProductDP_TLE(self, a: List[int]) -> int:
    
        n = len(a)
        dp = []
        
        for i in range(0, n):
            dp.append([0] * n)
        
        _max = -float('inf')
        for i in range(n - 1, -1, -1):
            for j in range(i, n):                
                if i == j:
                    dp[i][j] = a[i]
                else:
                    dp[i][j] = dp[i][j - 1] * a[j]
                    
                _max = max(_max, dp[i][j])
                
        return _max
                
