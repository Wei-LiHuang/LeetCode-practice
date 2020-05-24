# aware of line 25 to line 35


class Solution:
    
    def threeSum(self, a: List[int]) -> List[List[int]]:
        
        a.sort()        
        n = len(a)
        res = []
        
        for i in range(0, n):
            
            if a[i] > 0:
                break;
            
            if i > 0 and a[i] == a[i - 1]:
                continue            
            
            tgt = 0 - a[i]
            
            left = i + 1
            right = n - 1
            
            while left < right:
                _sum = a[left] + a[right]                
                    
                if _sum < tgt or (left > i + 1 and a[left] == a[left - 1]):
                    left += 1
                elif _sum > tgt or (right < n - 1 and a[right] == a[right + 1]):
                    right -= 1
                else:
                    res.append([a[i], a[left], a[right]])
                    left += 1
                    right -= 1                    
        
        return res
