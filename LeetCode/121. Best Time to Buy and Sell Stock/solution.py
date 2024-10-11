class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = prices[0]
        answer = 0

        for price in prices[1:]:
            if price < stock:
                stock = price
            else:
                profit = price - stock
                
                if profit > answer:
                    answer = profit
        
        return answer
        