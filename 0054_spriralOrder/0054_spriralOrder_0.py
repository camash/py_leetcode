def spiralOrder(matrix):
    res = []
    while matrix:
        # 削头（第一层）
        res += matrix.pop(0)
        # 将剩下的逆时针转九十度，等待下次被削
        matrix = list(zip(*matrix))[::-1]
    return res
