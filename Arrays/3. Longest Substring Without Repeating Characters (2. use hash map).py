class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        _dict = {}
        n = len(s)
        left = 0
        res = 0       

        for i in range(0, n):            
            c = s[i]            
            if c in _dict:
                left = max(_dict[c], left)
            
            _dict[c] = i + 1
            res = max(res, i - left + 1)
                                                                                
        return res
