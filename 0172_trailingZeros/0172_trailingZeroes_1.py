def trailingZeroes(n: int):
    if n < 5:
        return 0
    return n//5 + trailingZeroes(n//5)

if __name__ == '__main__':
    input = 50
    output = trailingZeroes(input)
    print(output)
