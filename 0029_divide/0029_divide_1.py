def divide(dividend: int, divisor: int):
    if dividend == -2147483648 and divisor == -1:
        return 2147483647

    sign = 1 if (dividend>=0 and divisor >0) or (dividend<0 and divisor<0) else -1
    dividend = -dividend if dividend < 0 else dividend
    divisor = divisor if divisor>0 else -divisor
    res = 0
    for i in range(31,-1, -1):
        # 被除数缩小2^i倍之后，突然小于divisor了，那么2^(i-1)刚好
        if (dividend >> i) - divisor >= 0:
            print(i)
            print(dividend >> i)
            dividend -= dividend - (divisor << i)
            res += (1 << i)

    return res if sign == 1 else 0 - res




if __name__ == '__main__':
    input1, input2 = 10, 3
    #input1, input2 = -2147483648, -1
    output = divide(input1, input2)
    print(output)
