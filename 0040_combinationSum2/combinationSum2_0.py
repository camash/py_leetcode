def combinationSum2(candidates: list, target:int):
    def dfs(candidates:list, s:int, target:int, cur:list, ans:list):
        if target == 0:
            ans.append(cur[:])
            return
        for i in range(s,len(candidates)):
            if candidates[i] > target:
                return
            # 下一个元素在递归中实现选取，避免在for循环中重复查询，通过i>s实现
            # 可以避免相同的情况筛选两次（一次原生For循环，一次是递归）
            if i > s and candidates[i] == candidates[i-1]:
                continue
            # 总和还小，加入当前值
            cur.append(candidates[i])
            # 从当前位的后面开始找 i+1
            dfs(candidates,i+1,target - candidates[i], cur, ans)
            # 一旦renturn pop掉最后的值，继续查找 (回溯操作)
            cur.pop()

    ans = []
    if sum(candidates) < target:
        return ans
    elif sum(candidates) == target:
        return [candidates]
    else:
        candidates.sort()
        dfs(candidates, 0, target, [], ans)
        return ans


if __name__ == '__main__':
    input1 = [1,1,1,1,1,2]
    print(sum(input1))
    input2 = 5
    output = combinationSum2(input1, input2)
    print(output)
