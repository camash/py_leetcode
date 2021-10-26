def plusone(digits: list):
    digits = [0] + digits
    n = len(digits)
    promo = 1
    for i in range(n-1,0,-1):
        promo, local = divmod(digits[i]+promo, 10)
        digits[i] = local
    if promo > 0:
        digits[0] = promo

    return digits if digits[0] > 0 else digits[1:]


if __name__ == "__main__":
    input = [9,9,9]
    output = plusone(input)
    print(output)