# 本题很难，主要是要考虑多种特殊情况：
# 长度为零
# 长度为一
# 元素的每一位都相等

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        min_str = sorted(strs, key=lambda x: len(x))[0]
        min_len = len(min_str)
        flag_loc = 0
        flag_1 = 0
        for i in range(0, min_len):
            for j in strs:
                if j[i] != min_str[i]:
                    flag_loc = i
                    flag_1 = 1
                    break
            else:
                continue
            break
        if flag_1 == 0:
            return min_str
        return min_str[:flag_loc]


if __name__ == '__main__':
    a = Solution()
    print(a.longestCommonPrefix(["c", "c", "c"]))
