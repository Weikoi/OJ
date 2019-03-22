class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        stat_dict = {}
        for i in s:
            if i in stat_dict:
                stat_dict[i] += 1
            else:
                stat_dict[i] = 1

        length = 0
        mid = 0
        for key, value in stat_dict.items():
            if value % 2 == 0:
                length += value
            else:
                mid = 1
                length += (value - 1)
        return mid + length