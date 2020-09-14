class Solution:
    def maxSumDivThree(self, a: List[int]) -> int:
        
        '''
            1. https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431057/Python-Math-Solution
                -> remove the smallest element that % 3 == (sum % 3)
                
            2. https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space
                -> record the maximum val of mod 3 == 0, 1, 2                
                -> [val mod 3 == 0, val mod 3 == 1, mod % 3 == 2]                            
        '''
        
        mod = [0, 0, 0]
        for e in a:
            for m in mod[:]:
                mod[(e + m) % 3] = max(mod[(e + m) % 3], e + m)

        return mod[0]

                
            
        
