class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        n = len(s)
        
        arr = [0] * 26
        dp = [arr[:]]                        
        for i in range(0, n):
            arr[ord(s[i]) - ord('a')] += 1            
            dp.append(arr[:])
        
        res = []
        for q in queries:            
            
            count = 0
            
            for i in range(0, 26):
                count += (dp[q[1] + 1][i] - dp[q[0]][i]) % 2
                
            if q[2] >= count // 2:
                res.append(True)
            else:
                res.append(False)
                
        return res
            
        
        
    def canMakePaliQueries_TLE(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        def countNeedSwapPair(s, i, j, k):
            
            d = dict()

            for x in range(i, j + 1):
                c = s[x]
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
                                                    
            left = 0
            for key in d.keys():                
                left += d[key] % 2
            
            return k >= (left // 2)
                                    
        res = []
        for q in queries:
            res.append(countNeedSwapPair(s, q[0], q[1], q[2]))

        return res
