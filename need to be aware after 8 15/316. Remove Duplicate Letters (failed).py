class Solution:
    def removeDuplicateLetters(self, a: str) -> str:
        
        n = len(a)
        
        d = dict()                
        for i in range(n - 1, -1, -1):            
            if a[i] not in d:
                d[a[i]] = list()
            d[a[i]].append(i)
                        
        used = set()
        stack = []        
        for i in range(0, len(a)):
            
            if a[i] not in used:
                while len(stack) > 0 and ord(a[i]) < ord(stack[-1]) and len(d[stack[-1]]) > 0 and d[stack[-1]][-1] > i - 1:
                    c = stack.pop()
                    used.remove(c)                        
                stack.append(a[i])
                used.add(a[i])
            
            d[a[i]].pop()
            
        return ''.join(stack)
            
