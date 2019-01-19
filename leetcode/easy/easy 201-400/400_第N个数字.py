class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        while True:
            first = 10**(digit-1)
            cnt = 9 * first * digit
            if cnt >= n:
                return int(str(first + (n-1)//digit)[(n-1) % digit])
            n -= cnt
            digit += 1