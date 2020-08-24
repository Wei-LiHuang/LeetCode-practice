class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        '''
            nums = 2, 3, 4, 5, 6, 8, 9, .....
            
            = 2, 4, 6 ,8, 10 ...
            + 3, 6, 9, 12, 15 ...
            + 5, 10, 15, 20, .....
        
        
            F(N) = a + b + c - a ∩ c - a ∩ b - b ∩ c + a ∩ b ∩ c
            F(N) = N/a + N/b + N/c - N/lcm(a, c) - N/lcm(a, b) - N/lcm(b, c) + N/lcm(a, b, c)(lcm = least common multiple)
            Find the least integer N that satisfies the condition F(N) >= K                
        '''
        
        
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        
        lcm1 = lcm(a, b)
        lcm2 = lcm(a, c)
        lcm3 = lcm(b, c)        
        lcm4 = lcm(a, lcm3)
        
        l, r = 1, 2 * (10 ** 9)
        while l < r:            
            mid = (l + r) // 2
            val = mid // a + mid // b + mid // c - mid // lcm2 - mid // lcm1 - mid // lcm3 + mid // lcm4
            if val < n:
                l = mid + 1
            else:
                r = mid

        return l
                
