def setZeros(matrix: list):
    row_set = set()
    col_set = set()
    for i in len(matrix):
        for j in len(matrix[i]):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    for i in len(matrix):
        for j in len(matrix[i]):
            if i in row_set or j in col_set:
                matrix[i][j] = 0


