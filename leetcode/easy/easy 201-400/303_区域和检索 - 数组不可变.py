class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

def __init__(self, nums):
    self.nums = nums
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    """
    :type nums: List[int]
    """


def sumRange(self, i, j):
    if i == 0:
        return self.nums[j]
    else:
        return self.nums[j] - self.nums[i - 1]
