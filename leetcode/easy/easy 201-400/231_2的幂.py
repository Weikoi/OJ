class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1:
            return True
        while (n % 2 == 0) and (n != 2):
            n = n / 2
        if n == 2:
            return True
        else:
            return False

    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n & (n - 1) == 0


if __name__ == '__main__':
    results = Solution()
    print(results.isPowerOfTwo(16))
