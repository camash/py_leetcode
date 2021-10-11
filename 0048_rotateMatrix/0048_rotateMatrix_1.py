def rotate(matrix: list):
    n = len(matrix)
    # 按y=x轴进行翻转,遍历左上角即可
    for i in range(n):
        for j in range(n-i):
            matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

    # 上下对折
    for i in range(n//2):
        for j in range(n):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

    print(matrix)

if __name__ == "__main__":
    input = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(input)
