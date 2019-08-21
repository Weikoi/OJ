import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        length = len(nums)
        import sys
        result = sys.maxsize
        min_value = sys.maxsize
        for idx in range(length):

            left = idx + 1
            right = len(nums) - 1

            while (left < right):
                three_sum = nums[idx] + nums[left] + nums[right]
                if abs(three_sum - target) < min_value:
                    result = three_sum
                    min_value = abs(three_sum - target)

                if three_sum == target:
                    return three_sum
                elif three_sum < target:
                    left += 1
                else:
                    right -= 1
        return result

if __name__ == '__main__':
    print(sys.maxsize)