class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n, cur, dt, diff, res = len(s), [0] * 256, [0] * 256, 0, ""
        
        for c in t:
            dt[ord(c)] += 1
            diff += 1
            
        minL, start = n + 1, 0
        #ADOBECODEBANC
        #0123456789
        for i in range(0, n):
            c = ord(s[i])
            cur[c] += 1
            
            if dt[c] > 0 and cur[c] <= dt[c]:                
                diff -= 1                
                if diff == 0:
                    if minL > i - start + 1:
                        minL = i - start + 1
                        res = s[start:i + 1]
                    cur[ord(s[start])] -= 1
                    diff += 1
                    start += 1
                    #move to next target
                    while start < n and dt[ord(s[start])] == 0:
                        cur[ord(s[start])] -= 1                        
                        start += 1
                            
            if start < n and dt[ord(s[start])] == 0:
                #move start to next target:
                while start < n and dt[ord(s[start])] == 0:                    
                    start += 1
            else:
                while start < n and cur[ord(s[start])] > dt[ord(s[start])]:
                    cur[ord(s[start])] -= 1
                    start += 1
                    while start < n and dt[ord(s[start])] == 0:
                        cur[ord(s[start])] -= 1                        
                        start += 1       
            
        return res
                    
