class Solution:
    
    def numDecodings(self, s: str) -> int:        
        n = len(s)                   
        dp = [0] * n        
        for i in range(n - 1, -1, -1):
        
            v1 = int(s[i])
            if v1 == 0:
                dp[i] = 0
                continue            
            if i == n - 1:
                dp[i] = 1
            else:                
                dp[i] = 0
                dp[i] += dp[i + 1]

                v2 = int(s[i: i + 2])
                if i <= n - 2 and v2 <= 26 and v2 >= 0:                                        
                    if i == n - 2:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i + 2]                                                                
        return dp[0]        
    def numDecodings_getAllString(self, s: str) -> int:
        
        def mapping(i):
            res = chr(ord("A") + (i - 1))
            return res
                
        n = len(s)
                                
        dp = [None] * n
        
        for i in range(n - 1, -1, -1):
        
            v1 = int(s[i])
            if v1 == 0:
                dp[i] = []
                continue
            
            if i == n - 1:
                dp[i] = [mapping(v1)]
                
            else:                
                dp[i] = []                
                c1 = mapping(v1)
                for seq in dp[i + 1]:
                    l = [c1]
                    l.extend(seq)
                    dp[i].append(l)
                
                v2 = int(s[i: i + 2])
                if i <= n - 2 and v2 <= 26 and v2 >= 0:
                    c2 = mapping(v2)
                    
                    if i == n - 2:
                        dp[i].append([c2])
                    else:
                        for seq in dp[i + 2]:
                            l = [c2]
                            l.extend(seq)
                            dp[i].append(l)
                                                                
        return len(dp[0])
