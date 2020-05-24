# you are guaranteed that there will always be only one unique minimum window in S, it not, return ""

# T: ABC
# S: ADOBECODEBANC

# A, AD, ADO, ADOB, ADOBE, ADOBEC(contains all T, update answer)
# ADOBECO, ADOBECOD, ADOBECODE, ADOBECODEB(B is in T, can we update left index? => no)
# ADOBECODEBA(A is in T, can we update left index? => yes ... move left index one by one) -> CODEBA
# CODEBAN, CODEBANC (C is in T, update left index)

# do we need to check if the solution exist? no, if we reach the end and no answer updated, return ans = ""

#idea is clear, coding takes too long.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        _t = [0] * 256
        diff = 0
        for c in t:        
            _t[ord(c)] += 1
            diff += 1
                        
        _s = [0] * 256
        left, n = 0, len(s)
        minL = n + 1
        res = ""
        for i in range(0, n):
            cur = s[i] 
            c = ord(cur)     
            
            _s[c] += 1
            if _t[c] != 0:
                #check diff:
                if _s[c] == _t[c]:
                    diff -= 1
                elif _s[c] < _t[c]:
                    diff -= 1
                else:
                    diff -= 0 #diff remains the same

                #check length:
                if diff == 0:
                    if minL > (i - left + 1):
                        minL, res = (i - left + 1), s[left:i+1]

                    _s[ord(s[left])] -= 1
                    diff += 1
                    left += 1
                    while left < n and _t[ord(s[left])] == 0:
                        _s[ord(s[left])] -= 1;
                        left += 1;
            
            
            #move left:
            if left < n and _t[ord(s[left])] == 0:
                while left < n and _t[ord(s[left])] == 0:
                    left += 1;
            else:
                while left < n and _s[ord(s[left])] > _t[ord(s[left])]:
                    _s[ord(s[left])] -= 1
                    left += 1
                    while left < n and _t[ord(s[left])] == 0:
                        _s[ord(s[left])] -= 1;
                        left += 1;                    
                
                                                                                                        
        return res
