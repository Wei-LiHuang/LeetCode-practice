class Solution:
    def rob(self, a: List[int]) -> int:
                
        def R(a, i, memo):
            
            if i >= len(a):
                return 0
            
            if memo[i] is not None:
                return memo[i]
            
            _max = max(R(a, i + 2, memo) + a[i], R(a, i + 1, memo))
            memo[i] = _max
            
            return _max
        
        n = len(a)
        
        if n == 0:
            return 0
        
        memo = [None] * n
        
        for i in range(n - 1, -1, -1):
            R(a, i, memo)
            
        return memo[0]
        
