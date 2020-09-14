class Solution:
    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        
        '''
            brute force:
             list out all the possible sub arrays:
                c[i][j] = the odd numbers in subarray a[i:j + 1]
                
                if i == j:
                
                    if a[i] is odd:
                        c[i][j] = 1
                    elif a[i] is even:
                        c[i][j] = 0                        
                else:
                    if a[i] is odd:
                        c[i][j] = 1 + c[i + 1][j]
                    elif a[i] is even:
                        c[i][j] = 0 + c[i + 1][j]
                        
                then count all c[i][j], if c[i][j] = k odds -> res += 1
                return res
                
            better sol:
                c = [0] * len(a)  -> which is the c[i][n - 1]
                c = [0] * (len(a) + 1), c[n] = 0
                for i in range(n - 1, -1, -1):
                    if a[i] is odd:
                        c[i] = 1 + c[i + 1]
                    elif a[i] is even:
                        c[i] = 0 + c[i + 1]
                        
                if odd count in a[i:j+1] == k -> res += 1
                    
                    odd count in a[i:j+1] = c[i] - c[j + 1]
                    
                    c[i] - c[j + 1] == k -> res += 1
                    
                    
                for i in range(n - 1, -1, -1):
                    if a[i] is odd:
                        c[i] = 1 + c[i + 1]
                    elif a[i] is even:
                        c[i] = 0 + c[i + 1]
                                                
                    after counting c[i], we check if any c[i] - k in dict
                        if true -> res += d[c[i] - k]
                        if false -> do nothing
                        
                    then we put c[i] in d                                                                                                            
        '''
        n = len(a)
        
        # c[i]: odd count in subarr a[i:n]
        c = [0] * (n + 1)
        
        # d[val]: how many val = c[k], k > i, appeared before i
        d = dict()        
        d[0] = 1
        
        res = 0
        for i in range(n - 1, -1, -1):            
            # count c
            if a[i] % 2 == 1:
                c[i] = c[i + 1] + 1
            else:
                c[i] = c[i + 1] + 0
                
            # check previous count: 
            # if in d has any c[i] - c[j + 1] == k, j >= i, the res should += 1
            # for any c[x], x > i, if c[x] == c[i] - k, res += d[c[x]]            
            if (c[i] - k) in d:
                res += d[(c[i] - k)]
                
            if c[i] in d:
                d[c[i]] += 1
            else:
                d[c[i]] = 1
        
        #print(c)
        #print(d)
        return res
