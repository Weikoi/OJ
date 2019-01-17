class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for idx in range(len(nums)):
            high = min(len(nums), idx + k + 1)
            demoset = set(nums[idx + 1:high])
            if nums[idx] in demoset:
                return True
        return False

    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict and i - numDict[nums[i]] <= k:
                return True
            else:
                numDict[nums[i]] = i
        return False
