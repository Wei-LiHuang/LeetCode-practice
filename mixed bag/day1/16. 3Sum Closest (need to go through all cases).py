# closest: need to try all?
# sort the array
# start from i = 0
# tgt = target - a[i], l = i + 1, r = n - 1
# while l < r, res = min(res, a[i] + a[l] + a[r] - target)

class Solution:
    def threeSumClosest(self, a: List[int], target: int) -> int:
        
        def twoSum(a, s, l, r, tgt, res):
            
            while l < r:                                
                val = a[s] + a[l] + a[r]
                diff = max(val, tgt) - min(val, tgt)
                if diff < res[0]:
                    res[0] = diff
                    res[1] = val
                    
                if val < tgt:
                    l += 1
                
                if val == tgt:
                    break
                
                if val > tgt:
                    r -= 1

        a.sort()
        res = [float('inf'), 0]
        for i in range(0, len(a)):
            twoSum(a, i, i + 1, len(a) - 1, target, res)
            
        return res[1]
            
