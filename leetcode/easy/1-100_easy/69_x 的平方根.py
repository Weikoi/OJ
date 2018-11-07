import time

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l_limit = 0
        r_limit = x
        while l_limit < r_limit:
            mid = int((l_limit + r_limit) / 2)
            if mid ** 2 > x:
                r_limit = mid
            else:
                l_limit = mid + 1
            print(l_limit, mid, r_limit)
            time.sleep(1)
        if l_limit > 1:
            return l_limit - 1
        else:
            return l_limit


if __name__ == '__main__':
    results = Solution()
    print(results.mySqrt(10000))
