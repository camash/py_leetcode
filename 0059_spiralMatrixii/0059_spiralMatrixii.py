def generateMatrix(n: int):
    mat = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    while left <= right and top <= bottom:
        # 从左至右
        for i in range(left, right+1):
            mat[top][i] = num
            num += 1
        # 从上至下
        for i in range(top+1, bottom+1):
            mat[i][right] = num
            num += 1
        # 从右到左
        for i in range(right-1, left-1, -1):
            mat[bottom][i] = num
            num += 1
        # 从下到上
        for i in range(bottom-1, top, -1):
            mat[i][left] = num
            num += 1
        top += 1
        left += 1
        right -= 1
        bottom -= 1

    return mat


if __name__ == '__main__':
    input = 10
    output = generateMatrix(input)
    print(output)
