class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1, 2]
        if n == 1:
            return nums[1]
        elif n == 2:
            return nums[2]
        for i in range(3, n + 1):
            nums.append(nums[i - 1] + nums[i - 2])
        return nums[n]


if __name__ == '__main__':
    results = Solution()
    print(results.climbStairs(7))
