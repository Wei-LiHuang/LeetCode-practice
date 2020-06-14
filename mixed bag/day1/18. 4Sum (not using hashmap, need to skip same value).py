# use 3 sum for four? Yes

# performance key point:  if tgt < a[t] + a[s] + a[l] + a[l] and tgt > a[t] + a[s] + a[r] + a[r]
# -> not important

# two sum 不用hashmap, 故有找到解的時候要檢查shifted l & r 是否需要再shift


class Solution:
    
    def fourSum(self, a: List[int], tgt: int) -> List[List[int]]:
        
        n = len(a)
        a.sort()
                
        def twoSum(a, tgt, t, s, l, r, res):
            
            if l > r:
                return 
            
            if tgt < a[t] + a[s] + a[l] + a[l]:
                return
            
            if tgt > a[t] + a[s] + a[r] + a[r]:
                return
            
            while l < r:
                _sum = a[t] + a[s] + a[l] + a[r]
                if tgt == _sum:
                    res.append([a[t], a[s], a[l], a[r]])
                    l += 1
                    r -= 1
                    while l > 0 and l < n and a[l] == a[l - 1]:
                        l += 1
                    while r < n - 1 and r >= 0 and a[r] == a[r + 1]:
                        r -= 1                        
                elif tgt < _sum:
                    r -= 1            
                elif tgt > _sum:
                    l += 1                                             
            return
                                                                                
        def threeSum(a, tgt, s, res):
            i = s + 1
            while i < n:
                twoSum(a, tgt, s, i, i + 1, n - 1, res)                
                i += 1
                while i > 0 and i < n and a[i] == a[i - 1]:
                    i += 1                                              
            return
                                
        fourRes = []
        i = 0
        while i < n:
            threeSum(a, tgt, i, fourRes)
            i += 1
            while i > 0 and i < n and a[i] == a[i - 1]:
                i += 1                    
                    
        return fourRes
            
