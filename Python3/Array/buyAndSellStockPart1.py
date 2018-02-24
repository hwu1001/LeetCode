# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    # Time: O(n)
    # Space: O(1)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        for p in prices:
            # Maintain our two tracking variables so we can find
            # our highest peak in profit after our lowest price
            minPrice = min(p, minPrice)
            profit = p - minPrice
            maxProfit = max(profit, maxProfit)
        return maxProfit

    # Time: O(n^2)
    # Space: O(1)
    # Time complexity is too high at O(n^2)
    def maxProfitBrute(self, prices):
        pLen = len(prices)
        maxPriceDiff = 0
        for i in range(pLen):
            for j in range(i + 1, pLen):
                res = prices[j] - prices[i]
                if res > maxPriceDiff:
                    maxPriceDiff = res
        return maxPriceDiff


if __name__ == "__main__":
    stockP = [7, 1, 5, 3, 6, 4]
    # stockP = [7, 6, 4, 3, 1]
    # stockP = [5,4,2,9,1,3]
    obj = Solution()
    print(obj.maxProfit(stockP))