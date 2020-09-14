class Solution:
    def removeKdigits(self, a: str, k: int) -> str:
        
        if k >= len(a):
            return "0"
        '''
            what is the local optimal choice?
                when no zero:
                    ex: 1432219
                        it will always be (n - 1) digits
                        987654321 -> remove 9
                        56789876  -> remove 9 -> remove the peak of the seq                        
                        123456 -> remove the peak = 6                        
                        654321 -> remove the peak = 6
                                                
                        1432219 -> peak1 = 4 -> 132219 -> 12219 -> 1219
                        
                when have zero:
                    still removing the peak
                    
                    
            so how to find the peak?
            
                1432219
                
                stack: [1, 0]
                stack: [1, 0] [4, 1] -> [4, 1]
                stack: [4, 1], [3, 2]
                stack: [4, 1], [3, 2], [2, 3]
                stack: [4, 1], [3, 2], [2, 3], [2, 4]
                stack: [4, 1], [3, 2], [2, 3], [2, 4], [1, 5]
                stack: [4, 1], [3, 2], [2, 3], [2, 4], [1, 5], [9, 6] -> stack: [4, 1], [3, 2], [2, 3], [2, 4], [9, 6]        
        '''        
        stack = []
        for i in range(0, len(a)):            
            if len(stack) == 0:
                stack.append(a[i])
                continue
            else:
                while k > 0 and len(stack) > 0 and stack[-1] > a[i]:
                    stack.pop()                
                    k -= 1            
                stack.append(a[i])
            #print(stack)
                
        if k > 0:
            stack = stack[0: len(stack) - k]
            
        leadZero = -1
        for i in range(0, len(stack)):
            if stack[i] == '0':
                leadZero = i
            else:
                break
            
        stack = stack[leadZero + 1:]
        
        if len(stack) == 0:
            return '0'
                                                                        
        return ''.join(stack)
            
