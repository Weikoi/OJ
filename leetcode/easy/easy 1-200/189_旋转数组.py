class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums[:l - k] = reversed(nums[:l - k])
        nums[l - k:] = reversed(nums[l - k:])
        nums[:] = reversed(nums)

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums[:] = nums[l - k:] + nums[:l - k]
