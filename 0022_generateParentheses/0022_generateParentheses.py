def generateParentheses(n: int):
    res_set = {'()',}
    for i in range(1,n):
        tmp_set = set()
        for item in res_set:
            for j in range(n):
                tmp_set.add(item[:j] + '()' + item[j:])
        res_set = tmp_set

    return list(res_set)


if __name__ == '__main__':
    input = 3
    output = generateParentheses(input)
    print(output)

