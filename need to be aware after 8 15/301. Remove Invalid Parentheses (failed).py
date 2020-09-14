class Solution:    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        # 1. get need del count:
        leftCount, rightCount, allRemoved = 0, 0, ""
        for i in range(0, len(s)):
            if s[i] == '(':                
                leftCount += 1
            elif s[i] == ')':
                if leftCount > 0:
                    leftCount -= 1
                else:
                    rightCount += 1   
            else:
                allRemoved += s[i]
                                    
        
        # 2. use dfs to do back tracking:        
        def dfs(s, curPath, index, dLeft, dRight, counter, res):            
            
            if index == len(s):                
                if counter == 0 and dLeft == 0 and dRight == 0:                    
                    res.add(''.join(curPath))
                return
        
            if s[index] == '(':                
                if dLeft > 0:
                    dfs(s, curPath, index + 1, dLeft - 1, dRight, counter, res)
                    
                curPath.append('(')                
                dfs(s, curPath, index + 1, dLeft, dRight, counter + 1, res)
                curPath.pop()
                
            elif s[index] == ')':
                if dRight > 0:                                        
                    dfs(s, curPath, index + 1, dLeft, dRight - 1, counter, res)
                
                if counter == 0:
                    return
                
                curPath.append(')')
                dfs(s, curPath, index + 1, dLeft, dRight, counter - 1, res)                            
                curPath.pop()
            
            else:
                curPath.append(s[index])
                dfs(s, curPath, index + 1, dLeft, dRight, counter, res)                            
                curPath.pop()
                
            return
        
        
        res = set()
        dfs(s, [], 0, leftCount, rightCount, 0, res)
        
        if len(res) == 0:
            return [allRemoved]
                
        return list(res)
