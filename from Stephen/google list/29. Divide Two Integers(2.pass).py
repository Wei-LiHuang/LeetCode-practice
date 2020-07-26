class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
                
        def rec(s1, s2, index, ans, l):
            
            if index >= len(ans):
                return
            
            _str = s1[0:l]
            _strLeft = s1[l:len(s1)]
            v1 = int(_str)
            v2 = int(s2)
                    
            if v1 < v2:                
                rec(s1, s2, index + 1, ans, len(s2) + 1)
            else:         
                back = 0
                count = 0
                while v1 >= v2:
                    v1 -= v2
                    count += 1
                ans[index] = count                
                newS1 = ""
                
                if v1 > 0:
                    newS1 = str(v1) + _strLeft
                    rec(newS1, s2, index + 1, ans, len(str(v1)) + 1)
                else:                                      
                    rec(_strLeft, s2, index + 1, ans, len(s2))
                
            return
            
                                                        
        # overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1        
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        
        isNeg = True
        if dividend < 0 and divisor < 0 or divisor > 0 and dividend > 0:
            isNeg = False
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend == divisor:
            if isNeg:
                return -1
            return 1
        elif dividend < divisor:
            return 0
        
        # dividend > divisor
        val1, val2 = str(dividend), str(divisor)        
        powOfTen1, powOfTen2 = len(val1) - 1, len(val2) - 1
        ans = [0] * (powOfTen1 - powOfTen2 + 1)
        
        rec(val1, val2, 0, ans, len(val2))
        
        res = 0
        p = len(ans) - 1
        for v in ans:
            res += v * 10 ** p
            p -= 1
        
        if isNeg:
            res = -res                
        return res
