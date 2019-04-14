class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 求dp[i][j]
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        if not obstacleGrid:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0 for i in range(m)] for i in range(n)]

        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]


if __name__ == '__main__':
    result = Solution()
    print(result.uniquePathsWithObstacles([[1, 0, 0]]))
