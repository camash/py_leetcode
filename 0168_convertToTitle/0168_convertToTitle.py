def convertToTitle(columnNumber: int):
    res = ""
    while columnNumber>0:
        columnNumber, cur = divmod((columnNumber-1), 26)
        # 从ascii码编号转化为字母
        res = chr(ord('A')+cur) + res

    return res


if __name__ == '__main__':
    input = 2147483647
    output = convertToTitle(input)
    print(output)



