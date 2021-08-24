def combinationSum2(candidates, target):
    slow,fast = 0

    for i in range(len(candidates)):
        j = i+1
        if