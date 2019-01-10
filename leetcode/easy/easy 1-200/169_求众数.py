class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for i in dic.keys():
            if dic[i] >(len(nums)//2):
                return i
