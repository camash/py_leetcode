def intToRoman(num):
    # 初始化表示符号
    normal_char = 'IXCM'
    middle_char = 'VLD'

    # 转换输入
    num_str = str(num)[::-1]

    roman_list = []
    #将数据翻转
    for i in range(len(num_str)):
        current_digit = int(num_str[i])
        if current_digit == 4:
            roman_list.append(normal_char[i] + middle_char[i])
        elif current_digit == 9:
            roman_list.append(normal_char[i] + normal_char[i+1])
        elif current_digit >= 5:
            roman_list.append(middle_char[i] + (current_digit - 5)*normal_char[i])
        else:
            roman_list.append(current_digit*normal_char[i])

    return "".join(reversed(roman_list))


if __name__ == "__main__":
    num = 1994
    print(intToRoman(num))



