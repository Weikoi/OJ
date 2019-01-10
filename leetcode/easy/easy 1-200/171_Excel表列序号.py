class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        s_list.reverse()
        num = 0
        for idx, i in enumerate(s_list):
            num += (ord(i) - 64) * (26 ** idx)
        return num


if __name__ == '__main__':
    result = Solution()
    print(result.titleToNumber('AE'))