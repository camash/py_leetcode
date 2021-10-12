def myPow(x: float, n: int):
    if n < 0:
        return myPow(1/x, abs(n))
    if n == 0:
        return 1
    if n == 1:
        return x
    return x*myPow(x, n-1)


if __name__ == '__main__':
    output = myPow(2.1, 3)
    print(output)