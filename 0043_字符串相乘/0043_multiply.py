def multiply(num1: str, num2: str):
    full_res = []
    num1 = num1[::-1]
    num2 = num2[::-1]
    for i in range(len(num1)):
        curr_str_list = []
        curr = 0
        promo = 0
        for j in range(len(num2)):
            promo, curr = divmod(int(num1[i]) * int(num2[j]) + promo, 10)
            curr_str_list = [curr] + curr_str_list
        full_res.append(curr_str_list + [0]*i)

    promo_list = [0]*(len(num1)+len(num2))
    for i in range(len(num1)+len(num2), -1, -1):
        curr_digit = 0
        for item in full_res:
            if not item:
                curr_digit += item.pop()





    return full_res


if __name__ == "__main__":
    input1 = "12"
    input2 = "3"
    output = multiply(input1, input2)
    print(output)






