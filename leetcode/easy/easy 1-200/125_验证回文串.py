class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        demo_list = []
        for i in s.lower():
            if i.isdigit() or i.isalpha():
                demo_list.append(i)
        return demo_list == demo_list[::-1]
