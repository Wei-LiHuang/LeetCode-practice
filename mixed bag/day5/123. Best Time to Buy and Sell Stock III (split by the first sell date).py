# res: for i = 0 ~ n - 1, find max (maximum possible Profit(sell at day or before day i) + maximum possible Profit(buy at day i or after day i) )

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
                
        def getMaximumPossibleProfit_SellBeforeOrAtDay_i(a):             
            
            n = len(a)            
            profit = [0] * n
            buyDate = 0
            
            #profit[0] must be 0, because must by at day 0, sell by day 0
            for sellDay in range(1, n):
                if a[sellDay] < a[buyDate]:
                    # if day sellDay is a better buy date
                    buyDate = sellDay                    
                profit[sellDay] = max(profit[sellDay - 1], a[sellDay] - a[buyDate])                
            
            return profit
        
        def getMaximumPossibleProfit_BuyafterOrAtDay_i(a):
            
            n = len(a)            
            profit = [0] * n
            sellDate = n - 1            
            #profit[n - 1] must be 0, because buy at day n - 1, sell at day n - 1
            for buyDay in range(n - 2, -1, -1):
                if a[buyDay] > a[sellDate]:
                    # if day i is a better sell date
                    sellDate = buyDay                    
                profit[buyDay] = max(profit[buyDay + 1], a[sellDate] - a[buyDay])                
            
            return profit
        
        
        seq1 = getMaximumPossibleProfit_SellBeforeOrAtDay_i(prices)
        seq2 = getMaximumPossibleProfit_BuyafterOrAtDay_i(prices)
        
        res = 0
        for i in range(0, len(prices)):
            res = max(res, seq1[i] + seq2[i])
        
        return res
                
