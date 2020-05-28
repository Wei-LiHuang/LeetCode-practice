class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = itemgetter(0))
        stack = []
        
        for i in intervals:
            if len(stack) == 0:
                stack.append(i)
            else:                
                if i[0] > stack[-1][1]:
                    stack.append(i)
                else:
                    stack[-1][1] = max(stack[-1][1], i[1])
        
        return stack
        
        
