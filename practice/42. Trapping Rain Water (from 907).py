class Solution:
    
    def trap(self, a: List[int]) -> int:
        
        '''
        res = sum of all the water each unit can stored on top        
            1. find the left highest index for each a[i]
            2. find the right highest index for each a[i]
            3. water = min(leftHeight[i], rightHeight[i]) * (dis = 1) - a[i]
        '''
        n = len(a)
        leftHighestIndex = [-1] * n
        rightHighestIndex = [n] * n
        
        stack = []
        for i in range(0, n):
            while len(stack) > 0 and a[stack[-1]] <= a[i]:
                stack.pop()            
            if len(stack) > 0:
                leftHighestIndex[i] = stack[0]
            stack.append(i)
            
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and a[stack[-1]] <= a[i]:
                stack.pop()            
            if len(stack) > 0:
                rightHighestIndex[i] = stack[0]
            stack.append(i)
            
            
        h = dict()
        h[-1] = 0
        h[n] = 0
        for i in range(0, n):
            h[i] = a[i]
            
        water = [0] * n
        for i in range(0, n):            
            waterHeight = min(h[leftHighestIndex[i]], h[rightHighestIndex[i]])
            if waterHeight > a[i]:
                water[i] = (waterHeight - a[i]) * 1
            
            
        return sum(water)
