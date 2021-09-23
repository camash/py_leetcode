def countAndSay(n: int):
    full_list = []
    if n == 1:
        return "1"
    full_list.append("1")
    for i in range(2,n+1):
        temp_str = ""
        temp_val = "-1"
        temp_cnt = 0
        for item in full_list[-1]:
            if temp_val != item:
                # 将上一个数字加入字符串
                if temp_val != "-1":
                    temp_str = temp_str + str(temp_cnt) + temp_val
                temp_val = item
                temp_cnt = 1
            else:
                temp_cnt += 1
        temp_str = temp_str + str(temp_cnt) + temp_val
        full_list.append(temp_str)

    return full_list[-1]


if __name__ == "__main__":
    input = 30
    output = countAndSay(input)
    print(output)






