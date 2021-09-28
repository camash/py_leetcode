def jump(nums: list):
    n = len(nums)
    # max_pos:目前能跳到的最远位置 end: 上次跳跃可达范围右边界（下次的最右起跳点）
    max_pos, end, step = 0, 0, 0
    for i in range(n-1):
        if max_pos >= i:
            max_pos = max(max_pos, i + nums[i])
            # 到达上次跳跃能到达的右边界了
            if i == end:
                print(i)
                # 目前能跳到的最远位置变成了下次起跳位置的有边界
                end = max_pos
                # 进入下一层跳跃
                step += 1
    return step


if __name__ == '__main__':
    input = [2,3,1,1,4]
    output = jump(input)
    print(output)
