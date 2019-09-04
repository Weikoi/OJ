class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def get_item(idx):

            if idx == 3:

                result.append(nums.copy())
                print(result)

            for i in range(idx, length):
                nums[idx], nums[i] = nums[i], nums[idx]
                get_item(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        length = len(nums)
        idx = 0

        result = []
        get_item(idx)

        return result


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
