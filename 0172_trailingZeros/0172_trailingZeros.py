import math
def trailingZeroes(n: int):
    add_zeroes = 0
    while n>0:
        add_zeroes += n//5
        n = n//5

    return add_zeroes



if __name__ == '__main__':
    input = 50
    output = trailingZeroes(input)
    print(output)