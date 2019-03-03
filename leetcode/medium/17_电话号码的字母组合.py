class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(maps[digits[0]])

        res = ['']
        for digit in digits:
            new_res = []
            for ch in maps[digit]:
                new_res.extend([ele + ch for ele in res])
                print(new_res)
            res = new_res
        return res


if __name__ == '__main__':
    results = Solution()
    print(results.letterCombinations("2356"))
