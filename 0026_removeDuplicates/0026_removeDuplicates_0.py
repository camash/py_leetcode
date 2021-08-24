def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    offset = 0
    for i in range(len(nums) - 1):
        if nums[i - offset] == nums[i + 1 - offset]:
            nums.pop(i+1 - offset)
            offset = offset + 1

    return len(nums)


if __name__ == '__main__':
    input_list = [0,0,1,1,1,2,2,3,3,4]
    len_out = removeDuplicates(input_list)
    print(len_out)