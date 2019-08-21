class Solution:
    def letterCombinations(self, digits: str):

        result = []
        if not digits:
            return result
        demo_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def find_result(string, digit):
            if not digit:
                result.append(string)
            else:
                for i in demo_dict[digit[0]]:
                    find_result(string + i, digit[1:])

        find_result('', digits)
        return result


if __name__ == '__main__':
    results = Solution()
    print(results.letterCombinations("2356"))
