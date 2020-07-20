class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        '''
            "lee(t(c)o)de)" -> lee(t(co)de) or lee(t(c)ode)                        
        '''
        
        stack = []
        n = len(s)
        
        needRemove = set()
        for i in range(0, n):            
            if s[i] == '(':
                stack.append(i)                                            
            elif s[i] == ')':                
                if len(stack) == 0:
                    needRemove.add(i)
                else:
                    stack.pop()
        
        for j in stack:
            needRemove.add(j)
        
        res = ""
        for i in range(0, n):
            if i not in needRemove:
                res += s[i]
                
        return res
            
