class Solution:
    
    def maxProfit(self, a: List[int]) -> int:
        
        if len(a) == 0:
            return 0
        
        buy = a[0]
        
        profit = 0
        for i in range(1, len(a)):
            if a[i] < buy:
                buy = a[i]
                
            if a[i] > buy:
                profit = max(profit, a[i] - buy)
                
        return profit
