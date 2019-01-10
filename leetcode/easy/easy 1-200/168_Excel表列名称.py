class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        #需要注意26时：26%26为0 也就是0为A 所以使用n-1  A的ASCII码为65
        """
        result = ""
        while n != 0:
            n = int(n)
            result = chr((n - 1) % 26 + 65) + result
            n = (n - 1) / 26
        return result


if __name__ == '__main__':
    result = Solution()
    print(result.convertToTitle(707))
