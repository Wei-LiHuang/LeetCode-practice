class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:                                    
        
        n = len(s)
        
        _set = set()
        for word in wordDict:
            _set.add(word)
                    
        dp = [False] * (n + 1)
        dp[n] = True
                
        for i in range(n - 1, -1, -1):            
            for j in range(n - 1, i - 1, -1):                
                subString = s[i: j + 1]
                if subString in _set and dp[j + 1]:
                    dp[i] = True
                    break
                    
        return dp[0]
                
                
        
                
