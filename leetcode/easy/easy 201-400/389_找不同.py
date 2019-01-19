class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_list = list(s)

        for i in list(t):
            if i in s_list:
                s_list.remove(i)
            else:
                return i

    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        new_list = list(s) + list(t)
        result = new_list[0]
        for i in new_list[1:]:
            result = result & i
        return result