# try 1: use dfs get permutaion list, break when reach k -> TLE
# try 2: count the numbers

class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        
        def rec(_list, k, path, res, memo):                        
            
            n, curLen = len(_list), len(path)            
            
            if curLen == n:
                res.append(path)
                return
                        
            unit = memo[n - curLen - 1]
            l = 0
            r = l + unit - 1
            
            for i in range(0, 9):                
                if _list[i] == 0:
                    continue                    
                if k >= l and k <= r:
                    # found digit:
                    path += str(i + 1)
                    _list[i] = 0
                    rec(_list, k - l, path, res, memo)
                    return  
                else:
                    l = r + 1
                    r = l + unit - 1
            return
                                                                                                            
        memo = dict()
        memo[0] = 1
        for i in range(1, n):
            memo[i] = memo[i - 1] * i
                                    
        res, _list = [], [1] * n
        rec(_list, k - 1, "", res, memo)
        
        return res[0]
        
        
        
        
        
