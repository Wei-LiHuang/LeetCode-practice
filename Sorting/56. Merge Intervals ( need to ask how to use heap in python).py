# sort by start time: stack:{[1,6]} , next: [8, 10] 
# 1. if next.start > stack.peek().end: push into stack
# 2. if next.start <= stack.peek().end: stack.peek().end = max(stack.peek().end, next.end)

# so how to sort by start time? unknow range => no O(N) sorting => just use build in sorting:
# need to ask how to use heap in python, like custom compare.

class Solution(object):

    def merge(self, a):
        
        a = sorted(a, lambda a1, a2 : a1[0] - a2[0])
        stack = []        
        for t in a:            
            if not stack:
                stack.append(t)                            
            elif t[0] > stack[-1][1]:
                stack.append(t)
            else:
                stack[-1][1] = max(stack[-1][1], t[1])
        
        return stack

        
