#tmmzuxt t tm tmm m mz mzu mzux mzuxt: fail to this twice, need to check the last round


class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
                        
        _dict = {}
        
        l = 0
        r = 0
        dis = 0
        n = len(s)
        
        if n == 0:
            return 0
        
        res = 1        
        while r < n:             
            
            cur = s[r]
            
            if s[r] not in _dict:
                _dict[s[r]] = r                
                r += 1                                
            else:        
                res = max(res, r - 1 - l + 1)                                                 
                moveTo = _dict[s[r]]
                while (l <= moveTo):
                    _dict.pop(s[l])
                    l += 1
        
        res = max(res, r - 1 - l + 1)
        
        return res
        
