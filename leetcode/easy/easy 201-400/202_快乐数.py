class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while True:
            n_list = list(str(n))
            n = sum([int(i)**2 for i in n_list])
            if n == 1:
                return True
            if n == 4:
                return False



