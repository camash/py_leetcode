def maxSubArray(nums):
    n = len(nums)
    for i in range(1,n):
        if nums[i-1] > 0:
            # 重新赋值，正向作用向后传递
            nums[i] = nums[i] + nums[i - 1]

    return max(nums)



if __name__ == '__main__':
    input = [-57,9,-72,-72,-62,45,-97,24,-39,35,-82,-4,-63,1]
    output = maxSubArray(input)
    print(output)

