def isPalindrome(x: int):
    # 有负号肯定不能匹配
    if x < 0:
        return False
    # 非零且末尾为零，调转后肯定不匹配
    elif x != 0 and x % 10 == 0:
        return False
    else:
        rightHalfRevert = 0
        while x > rightHalfRevert:
            # 求余得个位，将原数字提升一位（左移）
            rightHalfRevert = x % 10 + rightHalfRevert * 10
            # x 缩短一个数字
            x = x // 10

        # 偶数时直接相等，奇数时右边多一个个位
        return x == rightHalfRevert or x == rightHalfRevert//10

# 在Python中实际比str转换要来得慢
if __name__ == "__main__":
    x_in = 12121
    print(isPalindrome(x_in))
