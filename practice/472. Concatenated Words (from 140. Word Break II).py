class Solution:
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        def dfs(_set, s, r, memo):
            
            if r in memo and memo[r] == False:
                return False
            
            if r < 0:
                return True
            
            found = False
            
            for i in range(r, -1, -1):
                subStr = s[i:r + 1]
                if subStr in _set and dfs(_set, s, i - 1, memo):                    
                    found = True
                    break
                    
            memo[r] = found
            return found
            
                            
        def isConcatenatedWords(_set, curWord):
            n = len(curWord)
            memo = dict()
            return dfs(_set, curWord, n - 1, memo)
            
                                                            
        def cmp (w1, w2):
            return len(w1) - len(w2)
        
        words = sorted(words, key = cmp_to_key(cmp))
        #print(words)
        
        n = len(words)
        _set, res = set(), []
        for i in range(0, n):
            if i == 0:
                _set.add(words[i])
            else:                
                if isConcatenatedWords(_set, words[i]):
                    res.append(words[i])
                _set.add(words[i])
                    
        return res
