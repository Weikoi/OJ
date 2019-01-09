class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        demo_dict = {}
        for i in nums:
            if i in demo_dict.keys():
                demo_dict.pop(i)
            else:
                demo_dict[i] = 1
        return list(demo_dict.keys())[0]
