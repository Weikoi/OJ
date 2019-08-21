class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)

        result = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == -nums[idx]:
                    result.append([nums[idx], nums[left], nums[right]])
                    while (left < right and nums[left + 1] == nums[left]): left += 1
                    while (left < right and nums[right - 1] == nums[right]): right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[idx]:
                    left += 1
                elif nums[left] + nums[right] > -nums[idx]:
                    right -= 1
        return result


if __name__ == '__main__':
    print(Solution().threeSum([-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]))
