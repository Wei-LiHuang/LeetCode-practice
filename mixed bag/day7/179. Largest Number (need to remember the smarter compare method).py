class Solution:
    
    def largestNumber(self, a: List[int]) -> str:
        
        # return 0 -> v1 == v2, return 1 -> v1 > v2, return -1 -> v1 < v2 --> min to max
        # return 0 -> v1 == v2, return -1 -> v1 > v2, return 1 -> v1 < v2 --> max to min
        def sortByDigit(v1, v2):                        
            
            if v1 == v2:
                return 0
            
            sum1 = str(v1) + str(v2)
            sum2 = str(v2) + str(v1)
            
            if sum1 > sum2:
                return -1
            if sum1 < sum2:
                return 1
            
            return 0
        
        a = sorted(a, key=functools.cmp_to_key(sortByDigit))                    
        
        res = ""
        for i in range(0, len(a)):
            res += str(a[i])
            if res == "00":
                res = "0"
        
        return res
            
        
