class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0] * 365
        n = len(days)
        lastDay = days[n - 1]    
        
        needPay = set()
        for day in days:
            needPay.add(day - 1)
                        
        for i in range(365, 0, -1):            
            curDate = i - 1            
            if curDate == days[n - 1] - 1:
                dp[curDate] = min(costs)
                
            elif curDate < days[n - 1] - 1:
                c1, c7, c30 = 0, 0, 0                                                
                if (curDate + 1 <= 364):
                    c1 = dp[curDate + 1]
                if (curDate + 7 <= 364):
                    c7 = dp[curDate + 7]
                if (curDate + 30 <= 364):
                    c30 = dp[curDate + 30]
                    
                if curDate in needPay:                    
                    dp[curDate] = min([costs[0] + c1, costs[1] + c7, costs[2] + c30])
                else:
                    dp[curDate] = dp[curDate + 1]
                
        return dp[0]
            
