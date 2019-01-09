import time


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip()) == 0:
            return 0
        else:
            return len(s.split()[-1])


if __name__ == '__main__':
    results = Solution()
    time_s = time.clock()
    print(results.lengthOfLastWord('Hello World'))
    print(time.clock() - time_s)
