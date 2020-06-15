class Solution:
    
    def numTrees(self, n: int) -> int:
        
        def count(l, r, memo):
            
            d = r - l + 1
            
            if d in memo:
                return memo[d]
            
            res = 0                        
            if l > r:
                res = 0
            
            elif l == r:
                res =  1
                                        
            elif l == r - 1:
                res =  2
            
            else:                
                for i in range(l, r + 1):
                    
                    if i == l:
                        res += count(l + 1, r, memo) # 2
                    elif i == r:
                        res += count(l, r - 1, memo) # 2 
                    else:
                        res += count(l, i - 1, memo) * count(i + 1, r, memo)
                        
            memo[d] = res                                
            return res
        
        if n == 0:
            return 1
        
        memo = dict()
        
        return count(0, n - 1, memo)
                
