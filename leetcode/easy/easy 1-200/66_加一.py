import time


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_raw = ''
        for i in digits:
            str_raw = str_raw + str(i)

        int_raw = int(str_raw)

        int_plus = int_raw + 1
        str_plus_list = list(str(int(int_plus)))
        int_plus_list = [int(i) for i in str_plus_list]
        return int_plus_list


if __name__ == '__main__':
    results = Solution()
    time_s = time.clock()
    print(results.plusOne([4, 3, 2, 1]))
    print(time.clock() - time_s)
