# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# This question is actually quite simple once it's known that once we sell
# a stock, we're out of the stock at that price and must buy again. So the
# solution is the summation of all the positive, sequential deltas in the array

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
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit
    
    # Time: O(n)
    # Space: O(1)
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))

if __name__ == "__main__":
    # stockP = [7, 1, 5, 3, 6, 4] # 7
    stockP = [3,1,5] # 4
    obj = Solution()
    print(obj.maxProfit(stockP))