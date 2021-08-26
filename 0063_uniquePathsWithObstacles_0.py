def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0
    obstacleGrid[0][0] = 1
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = -1
    # 使出发点为1
    obstacleGrid[0][0] = 1
    for i in range(m):
        for j in range(n):
            # -1表示障碍，不变更其值
            if obstacleGrid[i][j] == -1:
                continue
            elif i == 0 and j == 0:
                continue
            # 首行遇到障碍，右侧的也为0
            elif i == 0:
                obstacleGrid[i][j] = max(obstacleGrid[i][j-1],0)
            elif j == 0:
                obstacleGrid[i][j] = max(obstacleGrid[i - 1][j], 0)
            else:
                # 求解非障碍节点时，若上一节点时障碍，则贡献路径为0
                obstacleGrid[i][j] = max(obstacleGrid[i-1][j],0) + max(obstacleGrid[i][j-1],0)

    return obstacleGrid[m-1][n-1]


if __name__ == '__main__':
    input = [[0,0],[1,1],[0,0]]
    output = uniquePathsWithObstacles(input)
    print(output)

