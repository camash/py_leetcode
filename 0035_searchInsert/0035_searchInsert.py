def searchInsert(nums: list, target: int):
    n = len(nums)
    if n == 1:
        if nums[0] >= target:
            return 0
        else:
            return 1

    if target >= nums[n//2]:
        return n//2 + searchInsert(nums[n//2:],target)
    else:
        return searchInsert(nums[0:n//2], target)


if __name__ == '__main__':
    input1 = [1,3,5,6]
    input2 = 7
    output = searchInsert(input1, input2)
    print(output)