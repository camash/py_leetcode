def permuteUnique(nums: list):
    def dfs(nums: list, cur:list, ans:list, pos:int):
        if len(cur) == len(nums):
            ans.append(cur[:])
            return
        for i in range(len(nums)):
            if pos <= i and nums[pos] == nums[i]:
                continue
            cur.append(nums[i])
            dfs(nums, cur, ans, i)
            cur.pop()
    ans = []
    nums.sort()
    dfs(nums, [], ans, 0)


if __name__  == "__main__":
    input = [1,2,3]
    ouput = permuteUnique(input)
    print(ouput)
