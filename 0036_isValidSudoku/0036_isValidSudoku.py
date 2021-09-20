def isValidSudoku(board: [[]]):
    temp_dict = {}
    # 行比较
    for i in range(9):
        temp_dict.clear()
        for j in range(9):
            if board[i][j] in temp_dict:
                temp_dict[board[i][j]] += 1
            else:
                temp_dict[board[i][j]] = 1
        for k in temp_dict.keys():
            if k != '.' and temp_dict[k] > 1:
                return False

    # 列比较
    for i in range(9):
        temp_dict.clear()
        for j in range(9):
            if board[j][i] in temp_dict:
                temp_dict[board[j][i]] += 1
            else:
                temp_dict[board[j][i]] = 1
        for k in temp_dict.keys():
            if k != '.' and temp_dict[k] > 1:
                return False

    # 方块比较
    seg_list = [[0,1,2], [3,4,5], [6,7,8]]
    for item_x in seg_list:
        for item_y in seg_list:
            temp_dict.clear()
            for i in item_x:
                for j in item_y:
                    if board[i][j] in temp_dict:
                        temp_dict[board[i][j]] += 1
                    else:
                        temp_dict[board[i][j]] = 1
            for k in temp_dict.keys():
                if k != '.' and temp_dict[k] > 1:
                    return False

    return True


if __name__ == '__main__':
    input = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    output = isValidSudoku(input)
    print(output)