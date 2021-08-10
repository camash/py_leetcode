def reverse(x):
    INT_MAX = pow(2,31)  - 1
    res = 0
    flag = 1 if x >0 else -1
    # 负值最大值直接溢出
    if x == -INT_MAX - 1:
        return 0
    x = abs(x)
    while (x != 0):
        remainder = x%10
        if (flag == 1 and (res > INT_MAX//10 or (res == INT_MAX//10 and remainder>7))):
            return 0
        elif (flag == -1 and (res > INT_MAX//10 or (res == INT_MAX//10 and remainder>8))):
            return 0

        res = res * 10 + remainder
        x = x // 10

    return res * flag

if __name__ == '__main__':
    result = reverse(-1230)
    print(result)

