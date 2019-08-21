
class Solution(object):
    # 标准答案
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i
                # print(dic)


# 第一题的标准答案就刷新三观，一遍遍历就做到了。

# 我的版本1
# def twoSum(self, nums, target):
#     dic = {}
#     for idx, num in enumerate(nums):
#         dic[num] = idx
#     for idx, num in enumerate(nums):
#         if target - num in nums:
#             return idx, dic[target - num]


if __name__ == '__main__':

    solution = Solution()
    print(solution.twoSum([8, 7, 6, 2, 1, 3, 9, 4, 5, 0], 17))
