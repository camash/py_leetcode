def divide(dividend: int, divisor: int):
    sign = 1 if (dividend>=0 and divisor >0) or (dividend<0 and divisor<0) else -1
    dividend = dividend if dividend < 0 else -dividend
    divisor = divisor if divisor>0 else -divisor
    if divisor == 1:
        return abs(dividend) if sign == 1 else -abs(dividend)
    i = 0
    while dividend + divisor <= 0:
        dividend += divisor
        i += 1
    return i if sign == 1 else -i


if __name__ == '__main__':
    input1, input2 = 7, -3
    #input1, input2 = -2147483648, -1
    output = divide(input1, input2)
    print(output)