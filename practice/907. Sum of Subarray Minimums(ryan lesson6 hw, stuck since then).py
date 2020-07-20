class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        
        '''
        Ryan lessson6: observe relationship between answers:
        
        From discusstion:        
            Drawing the N * N board and try to get the relationship of "a[i] is the min element in that pair"
            
            ex [3, 7, 8, 4]
            
                3   7   8   4
            3   3   3   3   3                
            7   x   7   7   4
            8   x   x   8   4
            4   x   x   x   4 
            
            -> find [smallerLeft, smallerRight] for each elements
                if smallerLeft is None  -> set to -1
                if smallerRight is None -> set to n
                
            a0: [-1,4], (0 - 1) * (4 - 0) * 3 = 12
            a1: [0, 3], (1 - 0) * (3 - 1) * 7 = 14
            a2: [1, 3], (2 - 1) * (3 - 2) * 8 = 8
            a3: [0, 4], (3 - 0) * (4 - 3) * 4 = 12
        '''
        
        n = len(a)
        leftAndRight = []
        for i in range(0, n):
            leftAndRight.append([-1, n])
        
        smallerLeft = collections.deque()
        for i in range(0, n):
            
            '''
             a[smallerLeft[0]] >= a[i]: for duplicate cases
            '''
            while len(smallerLeft) > 0 and a[smallerLeft[0]] >= a[i]:       
                smallerLeft.popleft()            
            if len(smallerLeft) > 0:
                leftAndRight[i][0] = smallerLeft[0]
                
            smallerLeft.appendleft(i)
        
        smallerRight = collections.deque()
        for i in range(n - 1, -1, -1):
            while len(smallerRight) > 0 and a[smallerRight[0]] > a[i]:
                smallerRight.popleft()            
            if len(smallerRight) > 0:
                leftAndRight[i][1] = smallerRight[0]
                
            smallerRight.appendleft(i)

        res = 0
        for i in range(0, n):
            res += (i - leftAndRight[i][0]) * (leftAndRight[i][1] - i) * a[i]
                                                
        return res % (10**9 + 7)
        
