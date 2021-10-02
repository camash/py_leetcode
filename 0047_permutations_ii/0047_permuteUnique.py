def permuteUnique(nums: list):
    def dfs(nums: list, cur:list, ans:list, used: list):
        if len(cur) == len(nums):
            ans.append(cur[:])
            return
        for i in range(len(nums)):
            # 首先当前节点未参与过
            if not used[i]:
                # 当前节点与上一节点相同，且上一节点还未使用
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                cur.append(nums[i])
                dfs(nums, cur, ans, used)
                used[i] = False
                cur.pop()
    ans = []
    used = [False]*len(nums)
    nums.sort()
    dfs(nums, [], ans, used)
    return ans


if __name__  == "__main__":
    input = [1,1,2]
    ouput = permuteUnique(input)
    print(ouput)
