class Solution:
        
    def rob(self, a: List[int]) -> int:
        
        def rec(a, start, memo):            
            if start >= len(a):
                return 0                        
            if start in memo:
                return memo[start]            
            memo[start] = max(rec(a, start + 2, memo) + a[start], rec(a, start + 1, memo))            
            
            return memo[start]
        
        
        # rob 0 ~ n - 2 v.s rob 1 ~ n - 1
        n = len(a)
        
        if n == 1:
            return a[0]
        
        a1 = a[0 : n - 1]
        memo = dict()
        rob1 = rec(a1, 0, memo)
        
        a2 = a[1 : n]
        memo2 = dict()
        rob2 = rec(a2, 0, memo2)
        
        return max(rob1, rob2)
