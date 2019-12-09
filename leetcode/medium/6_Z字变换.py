class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 1 or numRows <= 1:
            return s
        result = [''] * min(numRows, len(s))
        curr_row = 0
        go_down = 1
        for i in range(len(s)):
            result[curr_row] += s[i]
            if curr_row == 0:
                go_down = 1
            elif curr_row == numRows - 1:
                go_down = -1
            curr_row += go_down

        return "".join(result)

    def convert2(self, s, numRows):
        total_list = [[] for i in range(min(numRows, len(s)))]

        if numRows < 2:
            return s

        down = 1
        row = 0

        for i in s:
            total_list[row].append(i)
            if (down == 1 and row == numRows - 1) or (down == -1 and row == 0):
                down = -1 * down
            if down == 1:
                row += 1
            elif down == -1:
                row -= 1

        return_str = ""
        for each in total_list:
            return_str += "".join(each)

        return return_str


if __name__ == '__main__':
    print(Solution().convert2("LEETCODEISHIRING", 3))
