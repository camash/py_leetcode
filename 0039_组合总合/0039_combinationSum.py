def combinationSum(candidates: list, target: int):
    result = []
    get_comb(candidates, target, result)
    return result


def get_comb(in_list: list, out_sum: int, res: list):
    if len(in_list) == 0:
        return
    if len(in_list) == 1:
        if out_sum == in_list[0]:
            res.append(out_sum)
        else:
            return
    else:
        cur_val = in_list[0]
        a, b = divmod(out_sum, cur_val)
        if a > 0:
            for i in range(a+1):
                if i == 0:
                    if combinationSum(in_list[1:], out_sum):
                        res.append(combinationSum(in_list[1:], out_sum))
                else:
                    if combinationSum(in_list[1:], out_sum-cur_val*i):
                        res.append([cur_val]*i + combinationSum(in_list[1:], out_sum-cur_val*i))



if __name__ == '__main__':
    input1 = [2,3,6,7]
    input2 = 7
    output = combinationSum(input1, input2)
    print(output)