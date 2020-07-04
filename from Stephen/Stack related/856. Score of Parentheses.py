class Solution:
    
    def scoreOfParentheses(self, s: str) -> int:
                
        def rec(s, pair, i, j):
            if i == j - 1:
                return 1
            else:
                right1 = pair[i]
                if right1 == j:
                    return 2 * rec(s, pair, i + 1, j - 1)
                elif right1 < j:
                    return rec(s, pair, i, right1) + rec(s, pair, right1 + 1, j)
                                                
        n = len(s)
        if n == 0:
            return 0
        
        pair = dict()              
        stack = []
        for i in range(0, n):
            if s[i] == '(':
                stack.append(i)
            else:
                left = stack.pop()
                pair[left] = i
                                
        score = rec(s, pair, 0, n - 1)
                
        return score
