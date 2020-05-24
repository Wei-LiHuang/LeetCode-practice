# you are guaranteed that there will always be only one unique minimum window in S, it not, return ""

# T: ABC
# S: ADOBECODEBANC

# A, AD, ADO, ADOB, ADOBE, ADOBEC(contains all T, update answer)
# ADOBECO, ADOBECOD, ADOBECODE, ADOBECODEB(B is in T, can we update left index? => no)
# ADOBECODEBA(A is in T, can we update left index? => yes ... move left index one by one) -> CODEBA
# CODEBAN, CODEBANC (C is in T, update left index)

# do we need to check if the solution exist? no, if we reach the end and no answer updated, return ans = ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        _t = {}
        diff = 0
        for c in t:
            if c in _t:
                _t[c] += 1            
            else:
                _t[c] = 1
            diff += 1
                        
        n = len(s)        
        _s = {}
        minL = n + 1
        res = ""
        left = 0        
        for right in range(0, n):            
            
            cur = s[right]
                                    
            if cur in _s:
                _s[cur] += 1
            else:
                _s[cur] = 1
                                
            if cur in _t:        
                if _t[cur] > 0:
                    _t[cur] -= 1
                    diff -= 1                
                #can we move left?
                if _s[cur] > _t[cur] and s[left] == cur and diff == 0:                    
                    while (s[left] not in _t) or (_s[s[left]] > _t[s[left]]):
                        _s[s[left]] -= 1
                        if _s[s[left]] == 0:
                            _s.pop(s[left])
                        left += 1
                        
                if diff == 0 and right - left + 1 < minL:
                    minL = right - left + 1
                    res = s[left:right+1]                                                                    
        
        return res
