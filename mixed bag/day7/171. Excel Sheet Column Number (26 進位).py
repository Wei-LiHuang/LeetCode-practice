class Solution:    
    def titleToNumber(self, s: str) -> int:
        
        n = len(s)
        mul = 1
        res = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            val = ord(c) - ord('A') + 1
            res += val * mul
            mul *= 26
        
        return res
            
        
