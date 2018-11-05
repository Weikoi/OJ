"""
    考虑极端情况！尽量AK
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        if haystack == needle:
            return 0
        for idx in range(len(haystack)):
            if (idx + needle_len) <= (len(haystack)):
                if haystack[idx: idx + needle_len] == needle:
                    return idx
        return -1


if __name__ == '__main__':
    results = Solution()
    print(results.strStr("mississipi", "pi"))
