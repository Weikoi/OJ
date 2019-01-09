class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        matrix = [[1], [1, 1]]
        for i in range(2, numRows):
            eachrow = [0] * (i+1)
            eachrow[0] = 1
            eachrow[-1] = 1
            for j in range(1, i):
                eachrow[j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
            matrix.append(eachrow)
        return matrix


if __name__ == '__main__':
    result = Solution()
    print((result.generate(10)))
