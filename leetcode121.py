class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        all_profit = []
        cur_cheapest = prices[0]
        for price in prices:
            if price <= cur_cheapest:
                cur_cheapest = price
            else:
                profit = price - cur_cheapest
                all_profit.append(profit)
        if all_profit == []:
            return 0
        return max(all_profit)
