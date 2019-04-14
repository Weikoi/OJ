class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cur_max = [0 for i in range(len(nums))]
        cur_max[0] = nums[0]
        cur_max[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur_max[i] = max(cur_max[i - 2] + nums[i], cur_max[i - 1])
        return max(cur_max)


if __name__ == '__main__':
    result = Solution()
    print(result.rob([2, 7, 9, 3, 1]))
