def permute(nums: list):
    # 输入原数组，目标元素长度，当前数组，结果集
    def dfs(nums: list, n: int, cur: list, ans: list):
        if len(cur) == n:
            ans.append(cur[:])
            return
        # 遍历数据中的元素
        for i in range(len(nums)):
            # 剪枝
            if nums[i] in cur:
                continue
            cur.append(nums[i])
            dfs(nums, n, cur, ans)
            # 回溯
            cur.pop()


    ans = []
    dfs(nums, len(nums), [], ans)
    return ans


if __name__ == "__main__":
    input = [1]
    output = permute(input)
    print(output)