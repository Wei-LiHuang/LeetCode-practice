class Solution:
        
    def multiply(self, num1: str, num2: str) -> str:
        
        def toNum (s: str) -> int:
            n = len(s)
            res, power = 0, 0            
            for i in range(n - 1, - 1, -1):
                digit = (ord(s[i]) - ord('0'))
                res += digit * (10 ** power)
                power += 1
            return res
        
        def toStr (n: int) -> str:
            
            if n == 0:
                return "0"
            
            res = ""            
            power = int(math.log10(n))
            
            while power >= 0:                
                digit = int(n / (10 ** power))
                n -= digit * (10 ** power)                
                power -= 1
                res +=  chr(digit + ord('0'))
            
            return res

        
        n1 = toNum(num1)
        n2 = toNum(num2)
        
        res = n1 * n2
        
        return toStr(res)
        
