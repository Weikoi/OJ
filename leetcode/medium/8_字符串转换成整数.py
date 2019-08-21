class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        res = ''
        tmp = re.findall('^[-+]?[\d]+', str.strip())  # 正则判断，非法字符串会返回空，返回的必是带有一个+/-或无符号的数字串
        if tmp:
            ms = tmp[0]
            if ms[0] == "-" or ms[0] == "+":
                res = ms[1:]
            else:
                res = ms
            res = int(res)
            if ms[0] == "-":
                return max(-res, -0x80000000)
            return min(res, 0x7FFFFFFF)
        else:
            return 0

    def myAtoi2(self, str):
        """
        :type str: str
        :rtype: int
        """
        numset = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        op = {"-", "+"}
        if str == "" or str.isspace():
            return 0
        ms = str.lstrip()
        low = 0
        res = 0
        while low < len(ms) and ms[low] in op:  # 判断符号位是否正确
            low += 1
        if low > 1 or low == len(ms):
            return 0  # 只有符号没有数字，或者符号多于一个

        while low < len(ms):
            if ms[low] in numset:
                res = res * 10 + int(ms[low])
            else:
                break
            low += 1

        if ms[0] == "-":
            return max(-res, -2**31)
        return min(res, 2**31-1)

    def myAtoi3(self, str):
        import re
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)

if __name__ == '__main__':
    print(Solution().myAtoi3("words and 987"))
