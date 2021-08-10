def reverse(x):
    flag = 1
    if x<0:
        flag = -1
        x = x*flag
    x_str = str(x)
    res = int(x_str[::-1]) * flag

    if res > pow(2,31) - 1 or res< -pow(2,31):
        res = 0

    return res


if __name__ == '__main__':
    result = reverse(-1230)
    print(result)