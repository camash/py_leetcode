def nextPermutation(nums: list):
    min_val, max_val = min(nums), max(nums)
    n = len(nums)
    if min_val == max_val:
        return
    swap_flag = 0
    for i in range(n-1, 0, -1):
        if nums[i] > nums[i-1]:
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
            swap_flag = 1
            break

    if swap_flag == 0:
        temp = nums[0]
        for i in range(n//2):
            temp = nums[i]
            nums[i] = nums[n-i-1]
            nums[n-i-1] = temp

    print(nums)


if __name__ == '__main__':
    input = [1,3,2]
    output = nextPermutation(input)
    print(output)


