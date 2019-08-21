

class Solution(object):
    def romanToInt(self, s):
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum =0
        for i in range(len(s)-1):
            if dic[s[i]] >= dic[s[i+1]]:
                sum = sum + dic[s[i]]
            else:
                sum = sum - dic[s[i]]
        return sum + dic[s[-1]]


if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt('III'))
