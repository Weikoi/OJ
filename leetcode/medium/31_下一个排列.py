class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        down = 0
        flag = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                down = i - 1
                flag = 1
                break
        if not flag:
            nums.reverse()

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[down]:
                nums[i], nums[down] = nums[down], nums[i]
                last = nums[down + 1:]
                last.reverse()
                nums[down + 1:] = last


if __name__ == '__main__':
    results = Solution()
    print(results.nextPermutation())
