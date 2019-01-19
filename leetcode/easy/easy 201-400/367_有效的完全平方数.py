class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        low = 0
        high = num
        medium = (low + high) // 2
        while medium * medium != num:
            if medium * medium > num:
                high = medium
                medium = (low + high) // 2

            elif medium * medium < num:
                low = medium
                medium = (low + high) // 2

            if low == medium:
                return False
        return True

    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        low = 0
        high = num
        while low <= high:
            mid = (low+high)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                low = mid + 1
            elif mid **2 > num:
                high = mid - 1
        return False