def combinationSum(candidates: list, target: int):
    # s为查找起始位置
    def dfs(candidates, target, s, cur: list, ans):
        # 递归到target缩减为0，即退出
        if target == 0:
            ans.append(cur[:])
            return
        for i in range(s, len(candidates)):
            # 剪枝
            if candidates[i] > target:
                return
            cur.append(candidates[i])
            dfs(candidates, target - candidates[i], i, cur, ans)
            # 匹配或剪枝后都要退去最后位，重新查找匹配
            cur.pop()

    ans = []
    candidates.sort()
    dfs(candidates, target, 0, [], ans)
    return ans


if __name__ == '__main__':
    input1 = [2,3,6,7]
    input2 = 7
    output = combinationSum(input1, input2)
    print(output)

