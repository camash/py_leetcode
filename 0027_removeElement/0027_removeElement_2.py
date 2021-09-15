# 参考双指针处理
def removeElement(nums: list, val: int):
    n = len(nums)
    if n == 0:
        return 0
    i, j = 0, 0
    for j in range(n):
        # 相等，则把j指针继续向后移动0
        if nums[j] == val:
            continue
        else:
            # 将不能val的值赋值给i指针的位置，然后i向后移动一位
            nums[i] = nums[j]
            i += 1

    print(nums)
    return i


if __name__ == '__main__':
    input = [3, 2, 2, 3]
    val = 3
    output = removeElement(input, val)
    print(output)


