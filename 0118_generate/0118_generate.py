def generate(numRows: int):
    res = []
    for i in range(1,numRows+1):
        tmp_list = [1]*i
        for j in range(1,i-1):
            print(res[-1])
            tmp_list[j] = res[-1][j] + res[-1][j-1]
        res.append(tmp_list)

    return res


if __name__ == "__main__":
    input = 5
    output = generate(input)
    print(output)