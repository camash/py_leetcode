def search(nums,target):
    if not nums:
        return -1
    start, end = 0, len(nums) -1
    while start <= end:
        mid = (start + end)//2

        if nums[mid] == target:
            return mid

        # 情况1，左边有序
        if nums[start] <= nums[mid]:
            # 在有序范围内
            if nums[start] <= target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        # 右边有序
        else:
            if nums[mid+1] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid

    return -1


if __name__ == '__main__':
    input = [5,6,7,8,1,2,4]
    output = search(input, 1)
    print(output)

