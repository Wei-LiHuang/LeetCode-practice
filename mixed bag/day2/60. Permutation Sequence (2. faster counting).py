# try 1: use dfs get permutaion list, break when reach k -> TLE
# try 2: count the numbers

class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        
        def getLevel(tgt):
            res = 1
            for i in range(2, tgt + 1):
                res *= i
            return res
        
        def rec(nums, k, path):
            
            n = len(nums)
            
            #n = 4, unit = 6, 0 ~ 5: index = 1
            unit = getLevel(n - 1)
            seqIndex = k - 1
            digitIndex = seqIndex // unit            
            digit = nums[digitIndex]            
            nums = nums[0 : digitIndex] + nums[digitIndex + 1 : n]                        
            #debug:
            #print(nums)
            #print(unit)
            #print(seqIndex)
            #print(digitIndex)                                    
            path[0] += str(digit)
            k2 = k - digitIndex * unit            
            #print(k2)            
            if n - 1 > 0:
                rec(nums, k2, path)
                
            return
                                                                                            
        path = [""]
        
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
              
        rec(nums, k, path)
        return path[0]
        
