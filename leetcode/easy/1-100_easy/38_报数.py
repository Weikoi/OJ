class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict = {}
        dict[1] = '1'
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        for i in range(2, n+1):
            inner_dict = {}
            compare_to = dict[i - 1][0]
            count = 0
            for idx, j in enumerate(dict[i - 1]):
                if dict[i - 1][idx] == compare_to:
                    count += 1
                else:
                    inner_dict[compare_to] = count
                    count = 0
                    compare_to = dict[i - 1][idx]
            for k in [str(key) + str(value) for key, value in inner_dict.items()]:
                string = k + string
        print(dict)
        return dict[n]


if __name__ == '__main__':
    results = Solution()
    print(results.countAndSay(3))
