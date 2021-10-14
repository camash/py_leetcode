def canJump(nums: list):
    max_reach = 0
    for i in range(len(nums)):
        # 保证每个点都可以到达
        if i > max_reach:
            return False
        max_reach = max(i+nums[i], max_reach)

    return True


if __name__ == "__main__":
    input = [3,2,1,0,4]
    print(canJump(input))

