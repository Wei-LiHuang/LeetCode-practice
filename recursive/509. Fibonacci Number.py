class Solution:
    
    def fib(self, N: int) -> int:
        
        def rec(N: int, _dict: dict) -> int:
            
            if N in _dict:
                return _dict[N]
            
            else:            
                if N == 0:         
                    _dict[0] = 0
                    return 0
                elif N == 1:
                    _dict[1] = 1
                    return 1
                else:           
                    _dict[N] = rec(N - 1, _dict) + rec(N - 2, _dict)
                    return _dict[N]
        
        _dict = {}
        return rec(N, _dict)
            
        
