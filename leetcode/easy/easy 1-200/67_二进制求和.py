import time


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dig_sum = int(a, 2) + int(b, 2)  # 2进制转换成10进制求和
        return bin(dig_sum)[2:]  # 10进制转换成2进制时前两位为0b，需要去除


if __name__ == '__main__':
    results = Solution()
    time_s = time.clock()
    print(results.addBinary("11", '1'))
    print(time.clock() - time_s)
