class Solution:
    
    def maxSubarraySumCircular(self, a: List[int]) -> int:
        
        '''
        find a max subArray sum with a normal array:
        dp[i]: the maximum sum among the subarrays starting from a[i]
        (must contain a[i])        
        dp[i] = max(dp[i + 1] + a[i], a[i])
        
        -> is O(N)
        
        Now the array is Circular:
            brute force: for each element, create a new normal array, and get the answer -> O(N^2)
            
            
            from the discuss:
            max subArray Sum = (total sum - minimum middle SubarraySum) or maximum middle subarray sum
            
            reasons: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass                    
        '''
        inf = float('inf')
        maxSubArrSum, minSubArrSum, arrSum, = -inf, inf, 0
        curMax, curMin = -inf, inf
        
        for i in range(0, len(a)):
            arrSum += a[i]
            curMax = max(curMax + a[i], a[i])
            curMin = min(curMin + a[i], a[i])
            
            maxSubArrSum = max(curMax, maxSubArrSum)
            minSubArrSum = min(curMin, minSubArrSum)
        
        if maxSubArrSum < 0:
            return maxSubArrSum
        
        return max(maxSubArrSum, arrSum - minSubArrSum)
