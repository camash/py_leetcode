def myAtoi(s:str):
    s = s.strip()
    sign_int = 1
    result_int = 0
    for i in range(len(s)):
        if i == 0 and s[0] == '-':
            sign_int = -1
        elif i == 0 and s[0] == '+':
            sign_int = 1
        # 是数字
        elif 48 <= ord(s[i]) <= 57:
            result_int = result_int*10 + ord(s[i]) - 48
            if result_int >= 2**31:
                break
        # 非数字,退出循环
        else:
            break

    result_int = result_int * sign_int
    if result_int >= 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif result_int <= - 2 ** 31:
        return -2 ** 31
    else:
        return result_int


if __name__ == '__main__':
    s_in = '-91283472332'
    print(myAtoi(s_in))

