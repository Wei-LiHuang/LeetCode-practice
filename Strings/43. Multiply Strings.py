# power: **
# log: math.log10()
# int digit to char: chr(digit + ord('0'))

class Solution:
            
    def multiply(self, num1: str, num2: str) -> str:
        
        def turnNum(s: str) -> int:
            l = len(s)
            powerOfTen = 0
            val = 0
            for i in range(l - 1, -1, -1):
                digit = (ord(s[i]) - ord('0'))
                val += digit * (10 ** powerOfTen)
                powerOfTen += 1
            return val
        
        def turnStr(val: int) -> str:
            
            if val == 0:
                return "0"
            
            powerOfTen = int(math.log10(val))
            res = ""
            for p in range(powerOfTen, -1, -1):
                digit = int(val/(10 ** p))
                res += chr(ord('0') + digit)
                val -= digit * (10 ** p)
            return res
            
            
            
        val1 = turnNum(num1)
        val2 = turnNum(num2)
                        
        val3 = val1 * val2
        return turnStr(val3)
        
        
