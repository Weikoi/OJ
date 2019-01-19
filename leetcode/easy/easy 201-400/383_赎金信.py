"""
注意第三种做法，把字典的value设置成一个list，，最后遍历这个list来比对
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if set(ransomNote) > set(magazine):
            return False
        # char_dict = {}
        # for i in list(ransomNote):
        #     if i in char_dict:
        #         char_dict[i] += 1
        #     else:
        #         char_dict[i] = 1

        res = list(ransomNote)
        for i in list(magazine):
            if i in res:
                res.remove(i)
            else:
                pass
        if len(res) > 0:
            return False
        else:
            return True

    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if set(ransomNote) > set(magazine):
            return False
        char_dict = {}
        for i in list(ransomNote):
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        for i in list(magazine):
            if i in char_dict.keys():
                char_dict[i] -= 1
        for i in char_dict.values():
            if i > 0:
                return False
        return True

    def canConstruct3(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        table = {}
        for i in ransomNote:
            if i not in table:
                table[i] = [1, 0]
            else:
                table[i][0] += 1

        for i in magazine:
            if i in table:
                table[i][1] += 1

        for i, j in table.items():
            if j[0] > j[1]:
                return False
        return True


if __name__ == '__main__':
    result = Solution()
    print(result.canConstruct('bg', 'efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj'))
