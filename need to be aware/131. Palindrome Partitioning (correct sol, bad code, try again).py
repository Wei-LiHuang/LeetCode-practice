class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(s, left, isPalindrome, _dict):
            n = len(s)
            
            palindromeStartFromLeft = []
            for i in range(left, n):
                if isPalindrome[left][i]:
                    _str = ""
                    for c in range(left, i + 1):
                        _str += s[c]
                    
                    p = [_str]
                    for subStr in _dict[i + 1]:
                        sub = list(p)
                        sub.extend(subStr)
                        palindromeStartFromLeft.append(sub)
                        
            _dict[left] = palindromeStartFromLeft
            
            return
                
            
                
        n = len(s)
        dp = []
        for i in range(0, n):
            dp.append([0] * n)
                                
        for i in range(n - 1, -1, -1):
            
            for j in range(n - 1, i - 1, -1):
                
                dp[i][j] = False
                
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                    
        _dict =  dict()
        
        _dict[n] = [[]]
        
        for i in range(n - 1, -1, -1):
            dfs(s, i, dp, _dict)
            
            
        return _dict[0]
