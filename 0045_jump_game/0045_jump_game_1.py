def jump(nums: list):
    n = len(nums)
    # max_pos:目前能跳到的最远位置 end: 上次跳跃可达范围右边界（下次的最右起跳点）
    max_pos, end, step = 0, 0, 0
    # 从初始节点开始遍历，看达到最后节点前要经过的跳数，每次达到最远位置必须再次起跳，遍历完成跳了几次为最少跳数
    # 同时避免将最后一次落地算进去（不再起跳），所以遍历时不包含最后一个节点
    for i in range(n-1):
        print(i, nums[i], end='')
        print(':', end='')
        #if max_pos >= i:
        max_pos = max(max_pos, i + nums[i])
        print(max_pos)
        # 到达上次跳跃能到达的右边界了
        if i == end:
            # 目前能跳到的最远位置变成了下次起跳位置的有边界
            end = max_pos
            # 进入下一层跳跃
            step += 1
            print("end:"+str(end))
    return step


if __name__ == '__main__':
    input = [2,3,1,1,4]
    print(input)
    output = jump(input)
    print(output)
