class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxProfit=0
        cost=0
        n=len(prices)
        for i in range(n):
            cost=prices[i]-mini
            maxProfit=max(maxProfit,cost)
            mini=min(prices[i],mini)
        return maxProfit
        