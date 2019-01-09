"""
只能买卖一次
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_price = prices[1] - prices[0]
        for idx1, price1 in enumerate(prices[:-1]):
            for idx2, price2 in enumerate(prices[idx1 + 1:]):
                if price2 - price1 > max_price:
                    max_price = price2 - price1
        if max_price <= 0:
            return 0
        else:
            return max_price

    @staticmethod
    def maxProfit2(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        num = 0
        mins = prices[0]
        for i in prices:
            if i > mins:
                num = max(num, i - mins)
            else:
                mins = i
        return num

    @staticmethod
    def maxProfit3(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_p, max_p = prices[0], 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p


if __name__ == '__main__':
    result = Solution()
    print((result.maxProfit2([2, 2, 2, 2])))
