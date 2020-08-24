class Solution:
    def findBestValue(self, a: List[int], tgt: int) -> int:
        '''
            given a arr, pick one arbitary interger, 
            and change all the val in arr that bigger than the arbitary interger to it
        
            return the arbitary interger can make the closest sum to tgt
                            
            arbitary interger range:            
                min: 0
                max: max in arr (if bigger than max of arr, no val will change)
                                                
            the new sum of a will only going down,
                sum(a) >= sum(pick any integer) >= 0
                
                case1: tgt > sum(a) -> return max(a)
                
                case2: tgt == sum(a) -> return max(a)
                
                case3: tgt < sum(a):                
                    the possible ans will be one of s1 and s2, where s1 >= tgt, s2 <= tgt                    
                    -> sum(mid) = (sum(min), sum(max) = sum(a)) // 2
                                                                                                      
        '''        
        n = len(a)
        a.sort()
        
        sumPickMax = sum(a)
        sumPickMin = 0
        
        if sumPickMax <= tgt:
            return a[-1]
        
        l, r = 1, max(a)
        while l < r:
            mid = (l + r) // 2
            _sum = 0
            for i in range(0, n):
                _sum += min(mid, a[i])
                
            if _sum >= tgt:
                r = mid
            else:
                l = mid + 1
                
        s1, s2 = 0, 0
        for i in range(0, n):
            s1 += min(a[i], l)
            s2 += min(a[i], l - 1)
            
        if abs(s1 - tgt) >= abs(s2 - tgt):
            return l - 1
        else:
            return l
            
    
            
        
