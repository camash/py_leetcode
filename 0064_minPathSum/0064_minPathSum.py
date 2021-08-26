def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == j == 0:
                continue
            elif i ==0 and j > 0:
                # 首行的cost只能从左边值做累加
                grid[i][j] = grid[i][j] + grid[i][j - 1]
            elif j == 0 and i > 0:
                # 首列的cost只能从上面做累加
                grid[i][j] = grid[i][j] + grid[i-1][j]
            else:
                # 通用状态转移，从上方或者左边取cost较小的
                grid[i][j] = grid[i][j] + min(grid[i][j - 1], grid[i-1][j])

    return grid[m-1][n-1]


if __name__ == '__main__':
    input = [[1,3,1],[1,5,1],[4,2,1]]
    output = minPathSum(input)
    print(output)

