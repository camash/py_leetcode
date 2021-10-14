def canJump(nums: list):
    n = len(nums)
    if n == 1:
        return True
    least_pos = -1
    for i in range(n-1):
        if i + nums[i] >= n - 1:
            least_pos = i
            break
    if least_pos == -1:
        return False
    else:
        return canJump(nums[:least_pos+1])


if __name__ == "__main__":
    input = [3,2,1,0,4]
    print(canJump(input))
