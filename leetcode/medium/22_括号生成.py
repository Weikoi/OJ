class Solution:
    def generateParenthesis(self, n: int):
        # 回溯

        result = []

        def get_valid(s='', left=0, right=0):
            if len(s) == n * 2:
                print("add", s, result)
                result.append(s)

            if left < n:
                print("left", s,  result)
                get_valid(s + '(', left + 1, right)

            if right < left:
                print("right", s,  result)
                get_valid(s + ')', left, right + 1)

        get_valid()
        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
