def jump(nums: list):
    # 最后一个位置
    position = len(nums) - 1
    steps = 0
    while position > 0:
        for i in range(position):
            # 查找离position最远的能到达到的位置
            if i + nums[i] >= position:
                position = i
                steps += 1
                break
    return steps


if __name__ == '__main__':
    input = [2,3,1,1,4]
    output = jump(input)
    print(output)