class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = []
        _str = ""
        
        for i in range(0, len(s)):
            if s[i] == ' ':
                words.append(_str)
                _str = ""
                continue            
            _str += s[i]
            
        if _str != "":
            words.append(_str)
            
            
        if len(words) != len(pattern):
            return False
                        
        d, d2 = dict(), dict()
        
        for i in range(0, len(words)):
            p = pattern[i]
            w = words[i]
            
            if p not in d and w not in d2:
                d[p] = w
                d2[w] = p            
            elif p not in d:
                return False
            elif w not in d2:
                return False
            else:
                if d[p] != w or d2[w] != p:
                    return False
                                                                                    
        return True
        
