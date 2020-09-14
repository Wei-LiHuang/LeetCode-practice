# 推測: 無關黑洞, 就算全給a, 仍然TLE -> 可能方向錯誤 (0 -> n or n -> 0)



class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        n, _set = len(s), set()
        
        for w in wordDict:
            _set.add(w)
        
        dp = [None] * (n + 1)
        dp[n] = [""]
        
        for i in range(n - 1, -1, -1):                         
            for j in range(n - 1, i - 1, -1):
                
                subString = s[i: j + 1]                
                if subString in _set and dp[j + 1] is not None:
                    for nextSubString in dp[j + 1]:                        
                        #onePossible = [subString]
                        onePossible = subString                        
                        #onePossible.extend(nextSubString)
                        if len(nextSubString) > 0:
                            onePossible += " "
                        onePossible += nextSubString                                                
                        if dp[i] is None:
                            dp[i] = [onePossible]
                        else:
                            dp[i].append(onePossible)
                                                                
        if dp[0] is None:
            return []
                
        return dp[0]
                        
