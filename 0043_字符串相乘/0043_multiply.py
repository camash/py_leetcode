def multiply(num1: str, num2: str):
    if num1 == "0" or num2 == "0":
        return "0"
    full_res = ""
    num1 = num1[::-1]
    num2 = num2[::-1]
    # 从个位开始相乘
    for i in range(len(num1)):
        curr_str = ""
        curr = 0
        promo = 0
        # 从个位开始相乘
        for j in range(len(num2)):
            promo, curr = divmod(int(num1[i]) * int(num2[j]) + promo, 10)
            curr_str = str(curr) + curr_str
        # 按位置补0
        curr_str = curr_str + "0"*i
        # 有进位要加入
        if promo > 0:
            curr_str = str(promo) + curr_str
        print(full_res)
        full_res = add_two_strings(curr_str, full_res)

    return full_res


# 实现字符串相加的算法
def add_two_strings(str1: str, str2: str):
    n1 = len(str1)
    n2 = len(str2)
    if n1 < n2:
        add_two_strings(str2, str1)
    else:
        str1 = str1[::-1]
        str2 = str2[::-1]
        promo = 0
        curr = 0
        res = ""
        for i in range(n1):
            if i < n2:
                promo, curr = divmod(int(str1[i]) + int(str2[i]) + promo, 10)
            else:
                promo, curr = divmod(int(str1[i]) + promo, 10)
            # 当前位拼装
            res = str(curr) + res
        # 最终还有进位，加上
        if promo > 0:
            res = str(promo) + res
    return res



if __name__ == "__main__":
    input1 = "10488"
    input2 = "45600"
    output = add_two_strings(input1, input2)
    #output = multiply(input1, input2)
    print(output)






