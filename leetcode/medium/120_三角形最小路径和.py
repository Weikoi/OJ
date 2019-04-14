def minimumTotal(triangle) -> int:
    # 求dp[0,0]
    # dp[i, j] = min(dp[i+1,j], dp[i+1, j+1]) + V[i,j]

    print(triangle)
    if not triangle:
        return 0
    for i in range(len(triangle) - 2, -1, -1):
        print(i)
        for j in range(len(triangle[i]) - 1, -1, -1):
            print(j)
            triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        print(triangle)
    return triangle[0][0]


def minimumTotal2(triangle):

    dp = reversed([[0 for i in range(len(triangle[j]))] for j in range(len(triangle))])
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] 

if __name__ == '__main__':
    print(minimumTotal2([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]]))
