class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp = cur_min
        # dp[i] = min(dp[i-1]+v[i], dp[i-1]+v[i+1])

        if not cost:
            return 0

        dp = [i for i in cost]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1] + cost[i],dp[i - 2] + cost[i])
        return min(dp[-1], dp[-2])

if __name__ == '__main__':
    result = Solution()
    print(result.minCostClimbingStairs([0, 0, 1, 0]))
