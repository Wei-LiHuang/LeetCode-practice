class Solution:        
    def twoSum(self, a: List[int], tgt: int) -> List[int]:
        
        l, r = 0, len(a) - 1
        
        while l < r:
            cur = a[l] + a[r]
            if cur == tgt:
                return [l + 1, r + 1]
            elif cur > tgt:
                r -= 1
            else:
                l += 1
                
        return [-1, -1]
                
                
        
