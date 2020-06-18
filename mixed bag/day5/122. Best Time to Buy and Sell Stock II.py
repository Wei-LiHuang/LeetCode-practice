class Solution:
    
    def maxProfit(self, a: List[int]) -> int:
        
        if len(a) == 0:
            return 0
        
        buy = a[0]
        profit = 0
        for i in range(1, len(a) - 1):
            
            if buy > a[i]:
                buy = a[i]
                continue            
            if a[i] < a[i + 1]:
                continue
            else:
                profit += a[i] - buy
                buy = a[i + 1]
                
        if a[len(a) - 1] > buy:
            profit += (a[len(a) - 1] - buy)
                
                
        return profit
            
            
        
