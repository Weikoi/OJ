"""
    考虑极端情况！尽量AK
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        needle = 0
        if target < nums[0]:
            return 0
        for idx in range(len(nums)):
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                needle = idx
            else:
                return needle + 1
        return needle + 1


if __name__ == '__main__':
    results = Solution()
    print(results.searchInsert([1, 3, 5, 6], 4))
