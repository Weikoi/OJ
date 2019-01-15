"""
用正常方法的复杂度为o(n),
必须使用特殊方法，参考https://blog.csdn.net/github_39261590/article/details/73864039
中的算法，名为厄拉多塞算法，是筛查法的一种
"""

from math import sqrt


class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


if __name__ == '__main__':
    results = Solution()
    print(results.countPrimes(10))
