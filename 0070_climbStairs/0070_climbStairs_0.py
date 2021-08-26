def climbStairs(n):

    if n < 3:
        return n
    first = 1
    second = 2
    for i in range(3,n+1):
        third = first + second
        first = second
        second = third

    return second


if __name__ == '__main__':
    input = 3
    output = climbStairs(input)
    print(output)

