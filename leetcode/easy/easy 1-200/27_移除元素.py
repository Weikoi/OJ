class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if (len(nums) == 1 and nums[0] == val) or len(nums) == 0:
            return 0

        newidx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[newidx] = nums[i]
                newidx += 1
        return newidx


if __name__ == '__main__':
    results = Solution()
    # print(results.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(results.removeElement([3, 2, 2, 3], 3))
