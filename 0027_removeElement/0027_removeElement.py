# 不能修改原来引用的地址，所以该解法不能用

def removeElement(nums: list, val: int):
    print(hex(id(nums)))
    a_list = nums
    print(hex(id(a_list)))
    n = len(nums)
    cnt = 0
    for i in range(n):
        # 中间移到后面，则前面要补数
        if nums[i] == val:
            nums = [-1] + nums[:i] + nums[i+1:] + [val]
            cnt += 1
    nums = nums[cnt:]
    print(nums)
    print(a_list)
    print(hex(id(nums)))
    return n - cnt


if __name__ == '__main__':
    input = [3, 2, 2, 3]
    val = 3
    output = removeElement(input, val)
    print(output)


