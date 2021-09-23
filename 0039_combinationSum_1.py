def combinationSum(candidates: list, target:int):
    res = []
    if len(candidates) == 1:
        if candidates[0] == target:
            return res.append(candidates)

        else:
            return res

