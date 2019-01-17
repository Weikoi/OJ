class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.count(t) == self.count(s)

    def count(self, x):
        dic = {}
        for i in x:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 0
        return dic

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
