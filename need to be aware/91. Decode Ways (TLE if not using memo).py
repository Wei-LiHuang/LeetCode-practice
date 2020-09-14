class Solution:
    
    def numDecodings(self, s: str) -> int:
                
        def rec(s, l, r, d):                                    
            
            if r in memo:
                return memo[r]
            
            if r < l:
                return 1            
                        
            count = 0
            if int(s[r]) in d:
                count += rec(s, l, r - 1, d)                
            if r > 0 and s[r - 1] != '0' and int(s[r - 1:r + 1]) in d:
                count += rec(s, l, r - 2, d)            
                
            
            memo[r] = count
            return count
                                                                            
        d = dict()
        for i in range(1, 27):
            d[i] = chr(i - 1 + ord('A'))            
        #print(d)
        
        memo = dict()
        res = rec(s, 0, len(s) - 1, d)
                                
        return res
            
