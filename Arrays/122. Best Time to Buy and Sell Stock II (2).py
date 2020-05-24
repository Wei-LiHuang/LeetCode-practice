class Solution:
    
    def maxProfit(self, a: List[int]) -> int:
        
        n = len(a)
        buy = 0
        sell = 0
        profit = 0
        for i in range(0, n - 1):
            
            if a[i + 1] > a[i]:
                sell = i + 1
            if a[i + 1] <= a[i]:
                profit += a[sell] - a[buy]                
                buy = i + 1
                sell = buy
                
        profit += a[sell] - a[buy]
        
        return profit
    
