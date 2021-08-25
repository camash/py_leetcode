def maxSubArray(nums):
    n = len(nums)
    out_max = nums[0]
    res_list = []
    for i in range(1,n+1):
        # 通过边界截取
        l = 0
        while (l+i <= n):
            if sum(nums[l:l+i]) > out_max:
                out_max = sum(nums[l:l+i])
                #res_list = nums[l:l+i]
            # 递增边界
            l = l + 1

    return out_max


if __name__ == '__main__':
    input = [-2,1,-3,4,-1,2,1,-5,4]
    output = maxSubArray(input)
    print(output)