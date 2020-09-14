class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
            bookings[i] = [from i ~ j flights, k: number of seats]
            
            res = [0] * n                        
            1 ~ 2 -> 10
            2 ~ 3 -> 20
            2 ~ 5 -> 25            
            res = [10, 10 + 20 + 25, 20 + 25, 25, 25]
        '''
        '''
            1. straight forward sol:
                traverse the bookings, add the num to res directly
                -> O(len(bookings) * n) -> TLE
                
            2. could it be better?            
                sort the booking arr, merge the same booking
                but still O(len(bookings) * n) if the booking is not the same
                
            3. from discuss: https://leetcode.com/problems/corporate-flight-bookings/discuss/328871/C%2B%2BJava-with-picture-O(n)                
        '''
        
        _sum, res = [0] * n, [0] * n
        
        for booking in bookings:
            i, j, k = booking[0], booking[1], booking[2]
            _sum[i - 1] += k
            if j < n:
                _sum[j] += -k
            
        cur = 0
        for i in range(0, n):
            cur += _sum[i]
            res[i] = cur
                
            
                
                
        return res
        
