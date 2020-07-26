class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
            s: "cbaebabacd" p: "abc"
            diff = 3
            d[a] = 1, d[b] = 1, d[c] = 1
            in[a] = 0, in[b] = 0, in[c] = 0
            
            l = -1
            for i in range(0, n):
                if l == -1 and s[i] not in d:
                    continue
                elif: l == -1 and s[i] in d:
                    l = i                    
                    if in[s[i]] < d[s[i]]:
                        in[s[i]] += 1
                        diff -= 1
                        
                        if diff == 0:
                            res.append(l)
                            in[s[l]] -= 1
                            diff += 1
                            l = i + 1                                                
                    continue         
                    
                else:
                    if s[i] in d and in[s[i]] < d[s[i]]:
                        in[s[i]] += 1
                        diff -= 1                    
                        if diff == 0:
                            res.append(l)
                        in[s[l]] -= 1
                        diff += 1
                        l += 1
                    
                    elif s[i] in d and in[s[i]] == d[s[i]]:
                        while s[l] != s[i]:
                            in[s[l]] -= 1
                            diff += 1
                            l += 1
                    
                    elif s[i] not in d:
                        while l < i:                            
                            in[s[l]] -= 1
                            diff += 1
                            l += 1
                        l = i + 1                                                                                
        '''
        
        n = len(s)
        diff, d, count = 0, dict(), dict()
        for c in p:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                count[c] = 0                
            diff += 1                            

        res, l = [], -1
        for i in range(0, n):            
            if l == -1 and s[i] not in d:
                continue
                        
            elif l == -1 and s[i] in d:
                l = i                                    
                count[s[i]] += 1
                diff -= 1
                if diff == 0:
                    res.append(l)
                    count[s[l]] -= 1
                    diff += 1
                    l = i + 1                                                                        
            
            else:
                #print(s[l:i+1])
                
                if s[i] in d and count[s[i]] < d[s[i]]:
                    count[s[i]] += 1
                    diff -= 1                    
                    if diff == 0:
                        res.append(l)
                        count[s[l]] -= 1
                        diff += 1
                        l += 1

                elif s[i] in d and count[s[i]] == d[s[i]]:
                    while s[l] != s[i]:
                        count[s[l]] -= 1
                        diff += 1
                        l += 1
                    l += 1

                elif s[i] not in d:
                    while l < i:                            
                        count[s[l]] -= 1
                        diff += 1
                        l += 1
                    l = i + 1    
        
        return res
