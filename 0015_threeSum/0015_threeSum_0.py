def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    res = []
    for i in range(n):
        if nums[i] > 0:
            return res
        # 避免相同值与后面的L，R值出现相同的组合
        if i>0 and nums[i] == nums[i-1]:
            continue
        L = i+1
        R = n-1
        while L<R:
            if (nums[i] + nums[L] + nums[R])==0:
                res.append([nums[i], nums[L], nums[R]])
                # 避免相同值的情况，若元素相同直接跳过
                while (L<R and nums[L] == nums[L+1]):
                    L = L + 1
                while (L<R and nums[R] == nums[R-1]):
                    R = R - 1
                L = L + 1
                R = R - 1
            # 结果过大，则缩小大的值
            elif (nums[i] + nums[L] + nums[R]) > 0:
                R = R - 1
            else:
                L = L + 1

    return res


if __name__ == '__main__':
    input = [-1,0,1,2,-1,-4]
    output = threeSum(input)
    print(output)