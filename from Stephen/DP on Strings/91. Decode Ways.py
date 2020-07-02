class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(s, index, memo):
            
            if index == len(s):                
                memo[index] = 1
                return
            
            dfs(s, index + 1, memo)
            
            res = 0            
            
            v1 = int(s[index])                        
            if v1 == 0:
                memo[index] = 0
                return
            
            if v1 > 0 and v1 < 10:
                res += memo[index + 1]
                                        
            v2 = int(s[index : index + 2])
            if index < len(s) - 1 and v2 > 0:               
                if v2 <= 26 and v2 > 0:
                    res += memo[index + 2]
            
            memo[index] = res
            return
            


        memo = dict()
        dfs(s, 0, memo)
        
        return memo[0]
