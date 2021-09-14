def fourSum(nums: list, target: int):
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        if n - i <= 3:
            break
        res += [[nums[i]] + x for x in threeSum(nums[i+1:],target - nums[i])]

    return res


def threeSum(nums:list, target: int):
    n = len(nums)
    comb = []
    for i in range(n):
        # 相等则跳过
        if i>0 and nums[i] == nums[i-1]:
            continue
        L = i+1
        R = n-1
        while L<R:
            if nums[i] + nums[L] + nums[R] == target:
                comb.append([nums[i], nums[L], nums[R]])
                while L<R and nums[L] == nums[L+1]:
                    L = L+1
                while L<R and nums[R] == nums[R-1]:
                    R = R-1

                L = L +1
                R = R -1
            elif nums[i] + nums[L] + nums[R] > target:
                R = R -1
            else:
                L = L +1

    return comb


if __name__ == '__main__':
    input = [1,0,-1,0,-2,2]
    output = fourSum(input, 0)
    print(output)