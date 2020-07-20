class Solution:
    
    def largestRectangleArea(self, a: List[int]) -> int:
        
        '''
        for each a[i]:
            1. find the first smaller element on the left of a[i]
            2. find the first smaller element on the right of a[i]
            3. dis = (right - 1 - (left + 1) + 1)
            4. res = max(res, a[i] * dis)        
        '''
        n = len(a)
                
        firstSmallerOnLeft = [-1] * n
        firstSmallerOnRight = [n] * n
        
        stack = []
        for i in range(0, n):
            while len(stack) > 0 and a[stack[-1]] >= a[i]:
                stack.pop()            
            if len(stack) > 0:
                firstSmallerOnLeft[i] = stack[-1]
            stack.append(i)
            
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and a[stack[-1]] >= a[i]:
                stack.pop()            
            if len(stack) > 0:
                firstSmallerOnRight[i] = stack[-1]
            stack.append(i)
            
        res = 0
        for i in range(0, n):
            dis = (firstSmallerOnRight[i] - 1) - (firstSmallerOnLeft[i] + 1) + 1
            res = max(res, a[i] * dis)
                                            
        return res
