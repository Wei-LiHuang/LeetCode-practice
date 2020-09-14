class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        '''                 
            hint1 : arr is "in-order traversal" -> 順序不能變動
            hint2 : The value of each non-leaf node is equal to the product of the "largest leaf value in its left and right subtree" respectively           

            ex: 6,2,4,5               
                -> (((6, 2) 4), 5), (6, ((2, 4), 5)), ....                                                            
                
            from discuss:
                Given an array A, choose two neighbors in the array a and b,
                we can remove the smaller one min(a,b) and the cost is a * b.
        
                -> 對 a[i] 來說, 可以做得選擇是:
                    選一個 a[l], a[l] > a[i] 或 選擇一個 a[r], a[r] > a[i]
                    cost1 = a[i] * a[l]
                    cost2 = a[i] * a[r]
                    
                    對他們三個 a[i], a[l], a[r]來說, 結果都是留下 max(a[i], a[l], a[r])
                    但產生的cost會不同 -> 選cost最小的path
                    
            1. everytime we need to locate the min value, and find the first bigger on left, and on right -> then pick the smaller cost pair            
               finding min: O(n), find n times -> O(n^2)
                
            2. find the bigger left right for each node using stack:
                
                for each element in arr:
                    if stack is not empty and stack[-1] <= a[i]:
                        rightBigger = a[i]
                        middle = stack.pop()
                        if stack is empty:
                            res += middle * rightBigger
                        else:
                            res += middle * min(rightBigger, leftBigger)
                    stack.append(rightbigger = a[i])                                                                                                                                                
                if len(stack) > 2:
                    # merge from right to left
                    res += stack.pop() * stack[-1]                                
        '''
        
        res = 0
        stack = []
        for a in arr:
            while len(stack) > 0 and stack[-1] <= a:            
                middle = stack.pop()
                if len(stack) == 0:
                    res += middle * a
                else:
                    res += middle * min(a, stack[-1])
            stack.append(a)
        
        while len(stack) > 1:
            # merge from right to left
            res += stack.pop() * stack[-1]    

        return res
