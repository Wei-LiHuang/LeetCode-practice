class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def dfs(s, l, r, path, memo, _set, res):
            
            if r in memo and memo[r] == False:
                return False
                                        
            if r < l:                             
                _str = ""
                for j in range(0, len(path)):
                    _str += path[j]
                    if j != len(path) - 1:
                        _str += " "                    
                res.append(_str)
                return True
            
            found = False
            for i in range(r, -1, -1):
                subStr = s[i:r + 1]
                if subStr in _set:                
                    path.appendleft(subStr)
                    if dfs(s, 0, i - 1, path, memo, _set, res):
                        found = True
                    path.popleft()

            memo[r] = found                    
            return found
        
        _set = set(wordDict)
        memo = dict()
        res = []              
        path = collections.deque()        
        dfs(s, 0, len(s) - 1, path, memo, _set, res)
        
        return res
