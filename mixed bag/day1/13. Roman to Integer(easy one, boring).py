# boring question, can skip

# input : 1 ~ 3999

# M -> + 1000
# D -> + 500
# C -> C -> + 100, CM -> + 900 or CD -> + 400
# L -> L-> + 50
# X -> X -> +10, XC -> +90, XL -> +40
# V -> +5
# I -> 1 , 4, 9

class Solution:
    
    def romanToInt(self, s: str) -> int:
        res = 0
        i, n = 0, len(s)
        while i < len(s):
            c = s[i]
            
            if c == 'M':
                res += 1000
                i += 1
                continue
            
            if c == 'D':
                res += 500
                i += 1
                continue
            
            if c == 'C':                
                if i != n - 1:
                    if s[i + 1] == 'M':
                        res += 900                        
                        i += 2
                        continue
                    elif s[i + 1] == 'D':
                        res += 400
                        i += 2
                        continue
                res += 100
                i += 1
            
            if c == 'L':
                res += 50
                i += 1
                continue
            
            if c == 'X':
                if i != n - 1:
                    if s[i + 1] == 'C':
                        res += 90                     
                        i += 2
                        continue
                    elif s[i + 1] == 'L':
                        res += 40
                        i += 2
                        continue
                res += 10
                i += 1
                continue
            
            if c == 'V':
                res += 5
                i += 1
                continue
                
            if c == 'I':
                if i != n - 1:
                    if s[i + 1] == 'X':
                        res += 9                 
                        i += 2
                        continue
                    elif s[i + 1] == 'V':
                        res += 4
                        i += 2
                        continue
                res += 1
                i += 1
                continue
        
        
        return res
            
            
            
            
