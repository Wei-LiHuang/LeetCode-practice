class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        d = dict()
        for c in p:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        n, m, l = len(s), len(p), 0        
        '''
            0 ~ n - 1
            n - 1 - x + 1 = m
            x = n - m        
        '''        
        res = []
        while l <= (n - m):
            if s[l] not in d:
                l += 1
                continue
            else:                
                r = l
                count = dict()
                
                while r < n and s[r] in d and (s[r] not in count or count[s[r]] < d[s[r]]):
                    
                    if s[r] not in count:
                        count[s[r]] = 1
                    else:
                        count[s[r]] += 1                    
                        
                    if r - l + 1 == m:
                        res.append(l)                        
                        r += 1
                        while l < n and r < n and s[l] == s[r]:
                            res.append(l + 1)
                            l += 1
                            r += 1                                                    
                    else:
                        r += 1
                        
                if r < n and s[r] not in d:
                    l = r + 1
                else:  
                    l += 1
                
        return res
                
