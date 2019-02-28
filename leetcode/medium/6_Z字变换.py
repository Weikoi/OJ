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