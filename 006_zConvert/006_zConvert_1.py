def convert(s, numRows):
    if numRows==1:
        return s
    # 分成numRows行，每一行存放该行的字符
    compressed_list = ["" for _ in range(numRows)]
    # 如果我们把原始Z字形进行压缩，可以发现从s取数，然后不断变换方向往每一层放字符
    # flag表示方向，用于对索引进行变换
    i, flag = 0, 1
    for c in s:
        compressed_list[i] += c
        i = i+flag
        if i == 0 or i == numRows - 1:
            flag = -flag

    return "".join(compressed_list)

if __name__ == '__main__':
    result = convert("PAYPALISHIRING", 4)
    #result = convert("AB", 1)
    print(result)
    #PINALSIGYAHRPI