def addBinary(a: str, b: str):
    len_a = len(a)
    len_b = len(b)
    if len_b > len_a:
        return addBinary(b, a)

    b = '0'*(len_a - len_b) + b
    promote = 0
    c = ""
    for i in range(len_a-1, -1, -1):
        promote, temp_digit = divmod(int(a[i]) + int(b[i]) + promote, 2)
        c = str(temp_digit) + c
    if promote > 0:
        c = str(promote) + c

    return c


if __name__ == "__main__":
    input1 = "11"
    input2 = "1"
    print(addBinary(input1, input2))