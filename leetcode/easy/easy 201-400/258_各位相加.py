class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(list(str(num))) > 1:
            num = sum([int(i) for i in list(str(num))])
        return num


if __name__ == '__main__':
    result = Solution()
    print(result.addDigits(38))
