def combinationSum2(candidates: list, target:int):
    def dfs(candidates:list, s:int, target:int, cur:list, ans:list):
        if target == 0:
            # 原始数据中有重复数据的情况
            if cur not in ans:
                ans.append(cur[:])
            return
        for i in range(s,len(candidates)):
            if candidates[i] > target:
                return
            # 总和还小，加入当前值
            cur.append(candidates[i])
            # 从当前位的后面开始找 i+1
            dfs(candidates,i+1,target - candidates[i], cur, ans)
            # 一旦renturn pop掉最后的值，继续查找
            cur.pop()

    ans = []
    candidates.sort()
    dfs(candidates, 0, target, [], ans)
    return ans


if __name__ == '__main__':
    input1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    input2 = 27
    output = combinationSum2(input1, input2)
    print(output)
