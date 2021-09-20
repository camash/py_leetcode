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
        for k in range(9):
            if temp_dict[board[i][j]] > 1:
                return False

    # 列比较
    for i in range(9):
        temp_dict.clear()
        for j in range(9):
            if board[j][i] in temp_dict:
                temp_dict[board[j][i]] += 1
            else:
                temp_dict[board[j][i]] = 1
        for k in range(9):
            if temp_dict[board[j][i]] > 1:
                return False

    # 方块比较
    seg_list = [[0,1,2], [3,4,5], [6,7,8]]
    for item_x in seg_list:
        for item_y in seg_list:
            for i in item_x:
                temp_dict.clear()
                for j in item_y:
                    if board[i][j] in temp_dict:
                        temp_dict[board[i][j]] += 1
                    else:
                        temp_dict[board[i][j]] = 1
            for k in range(9):
                if temp_dict[k] > 1:
                    return False

    return True