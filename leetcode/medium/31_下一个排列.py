class Solution:
    def swap(self, nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
        return nums

    def reverse_part(self, nums, idx1):
        return nums[:idx1 + 1] + list(reversed(nums[idx1 + 1:]))

    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        idx1 = len(nums) - 2

        while idx1 >= 0 and nums[idx1] >= nums[idx1 + 1]:
            idx1 -= 1

        idx2 = len(nums) - 1
        while idx2 > idx1 and nums[idx2] <= nums[idx1]:
            idx2 -= 1
        nums1 = self.swap(nums, idx1, idx2)
        nums2 = self.reverse_part(nums1, idx1)

        return nums2


if __name__ == '__main__':
    results = Solution()
    print(results.nextPermutation([1, 3, 2]))
