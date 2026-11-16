class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mp = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             p = prices[i+1] - prices[i-1]
        #             mp = max(mp , prices[j] - prices[i])
        # l = 0
        # while l<r:
        #     r = 1
        #     mp = max(mp, prices[r]-prices[l])
        #     if prices
        p = prices
        mp = []
        for i in range(len(p)-1):
            pf = p[i+1] - p[i]
            if pf > 0:
                mp.append(pf)

        return sum(mp)