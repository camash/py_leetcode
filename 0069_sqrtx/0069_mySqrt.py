def mySqrt(x: int):
    left, right, res = 0, x, -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            res = mid
            left = mid + 1
        else:
            right = mid - 1

    return res
