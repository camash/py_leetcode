def rotate(matrix: list):
    n = len(matrix)
    matrix_new = [[0]* n for _ in range(n) ]
    # 规则，第一行换到最后一列，第二行换到倒数第二列
    for i in range(n):
        for j in range(n):
            matrix_new[j][n-1-i] = matrix[i][j]

    matrix[:] = matrix_new
    print(matrix)


if __name__ == "__main__":
    input = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(input)
