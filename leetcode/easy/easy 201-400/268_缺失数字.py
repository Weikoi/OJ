class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        com_list = [i for i in range(len(nums) + 1)]
        for i, j in zip(sorted(nums), com_list):
            if i != j:
                return j
        return com_list[-1]

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for idx in range(len(nums) + 1):
            result = (result ^ nums[idx]) ^ idx
        return result


if __name__ == '__main__':
    results = Solution()
    print(results.missingNumber2([0, 1, 3, 4]))
