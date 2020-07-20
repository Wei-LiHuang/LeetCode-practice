class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        '''
        dp[i]: 
            True: the sub string started from s[i] is a combination of words in wordDict
            False: the sub string started from s[i] is not a combination of words in wordDict            
        return dp[0]
                
        dp[i]:
            found = False
            for j in range(i + 1, n): 
                if s.subStr(i, j) in wordDict and dp[j] == True:
                    found = True
                    break            
            
            dp[i] = found
            
        -> runtime: O(N^2), space: O(N)        
        '''
        
        _set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                subStr = s[i:j]
                if subStr in _set and dp[j]:
                    dp[i] = True
                    break                    
        return dp[0]
                
