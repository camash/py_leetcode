def convert(s, numRows):
    column_list = []
    temp_column = ['' for n in range(numRows)]
    if numRows == 1:
        return s
    # 图形按照v形方式组合
    len_of_v = numRows + numRows - 2
    for i in range(len(s)):
        if i%len_of_v < numRows - 1:
            temp_column[i%len_of_v] = s[i]
        elif i%len_of_v == numRows - 1:
            temp_column[i%len_of_v] = s[i]
            column_list.append(temp_column)
            temp_column = ['' for n in range(numRows)]
        else:
            # 注意：斜线处是从大到小赋值的
            temp_column[numRows - 1 - (i%len_of_v - numRows + 1)] = s[i]
            column_list.append(temp_column)
            temp_column = ['' for n in range(numRows)]
    # 可能存在小于numRows的存在
    column_list.append(temp_column)

    # 转换出结果
    res = ''
    for i in range(numRows):
        for j in range(len(column_list)):
            res = res + column_list[j][i]


    print(column_list)
    return res




if __name__ == '__main__':
    #result = convert("PAYPALISHIRING", 4)
    result = convert("AB", 1)
    print(result)
    #PINALSIGYAHRPI