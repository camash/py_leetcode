def uniquePaths(m,n):
    #初始化转移矩阵，使一行一列固定为1，即到达该点只有一种走法
    path_matrix = [[1]*n] + [[1] + [0]*(n-1)]*(m-1)

    # 开始状态转换
    for i in range(1,m):
        for j in range(1,n):
            path_matrix[i][j] = path_matrix[i-1][j] + path_matrix[i][j-1]

    return path_matrix[m-1][n-1]


if __name__ == '__main__':
    output = uniquePaths(3,7)
    print(output)