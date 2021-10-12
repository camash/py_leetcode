def myPow(x: float, n: int):
    def quickMultiple(n):
        if n == 0:
            return 1.0
        y = quickMultiple(n//2)
        return y*y if n%2 == 0 else y*y*x

    return quickMultiple(n) if n >= 0 else 1/quickMultiple(-n)


if __name__ == '__main__':
    output = myPow(2.1, 3)
    print(output)

