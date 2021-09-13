def letterCombinations(digits:str):
    digi_dict = {}
    init_ascii = ord('a')
    for i in range(0,8):
        temp_str = chr(init_ascii) + chr(init_ascii+1) + chr(init_ascii+2)
        init_ascii += 3
        if i == 5 or i == 7:
            temp_str += chr(init_ascii)
            init_ascii += 1
        digi_dict[str(i+2)] = temp_str

    def listTimes(org: list, suf: str):
        # 初始元素，直接放入数组
        if not org:
            return [x for x in suf]
        else:
            res = []
            for item in org:
                for s in suf:
                    res.append(item+s)
            return res

    combo = []
    for s in digits:
        combo = listTimes(combo, digi_dict[s])

    return combo





if __name__ == '__main__':
    input = '23'
    output = letterCombinations(input)
    print(output)