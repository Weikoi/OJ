class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num & (num - 1) != 0:
            return False
        return (num & 0x55555555) != 0
