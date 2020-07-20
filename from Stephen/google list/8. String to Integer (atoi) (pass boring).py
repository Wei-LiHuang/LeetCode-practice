class Solution:
    def myAtoi(self, s: str) -> int:
        
        isNeg = None
        stack = []
        for c in s:
            if c == ' ':
                if len(stack) > 0 or isNeg is not None:
                    break
                continue                
            elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                stack.append(c)
            elif ord(c) == ord('-') or ord(c) == ord('+'):
                if ord(c) == ord('-') and isNeg == None and len(stack) == 0:
                    isNeg = True
                elif ord(c) == ord('+') and isNeg == None and len(stack) == 0:
                    isNeg = False
                else:
                    break
            else:
                break
        
        res = 0
        powOfTen = 0
        for i in range(len(stack) - 1, -1, -1):
            val = ord(stack[i]) - ord('0')
            res += (val * 10 ** powOfTen)
            powOfTen += 1
        
        if isNeg:
            res *= -1
        
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        else:
            return res
        
