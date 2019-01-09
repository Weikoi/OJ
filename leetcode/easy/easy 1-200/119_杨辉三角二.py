class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex==0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        matrix = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            eachrow = [0] * (i+1)
            eachrow[0] = 1
            eachrow[-1] = 1
            for j in range(1, i):
                eachrow[j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
            matrix.append(eachrow)
        return matrix[rowIndex]