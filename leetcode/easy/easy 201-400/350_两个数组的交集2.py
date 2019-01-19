class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dict = {}
        for num in nums1:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        for num in nums2:
            if num in dict and dict[num] > 0:
                dict[num] -= 1
                res.append(num)
        return res
