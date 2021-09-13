def threeSumClosest(nums: list, target: int):
    n = len(nums)
    nums.sort()
    best = 10**6

    def update(cur: int):
        nonlocal best
        if abs(cur - target) < abs(best - target):
            best = cur

    for i in range(n-2):
        j, k = i+1, n-1
        while j != k:
            if nums[i] + nums[j] + nums[k] == target:
                return target
            # 缩小和值, k--
            elif nums[i] + nums[j] + nums[k] > target:
                update(nums[i] + nums[j] + nums[k])
                k -= 1
            # 增大和值 j++
            else:
                update(nums[i] + nums[j] + nums[k])
                j += 1

    return best


if __name__ == '__main__':
    input = [-1,2,1,-4]
    target = 1
    output = threeSumClosest(input, target)
    print(output)
