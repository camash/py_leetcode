def subsets(nums):
    result = []
    nums.sort()
    # +1为了全员的也要找一次
    for i in range(len(nums) + 1):
        result = result + combine(nums, i)

    return result


def combine(nums, k):
    temp_list = []
    search_list = []
    backtracking(nums, k, temp_list, 0, search_list)
    return temp_list


def backtracking(nums, k, temp_list, begin, search_list):
    if len(search_list) == k:
        temp_list.append(search_list.copy())
        return
    for j in range(begin, len(nums)):
        search_list.append(nums[j])
        backtracking(nums, k, temp_list, j+1, search_list)
        search_list.pop()


if __name__ == '__main__':
    output = subsets([1,2,3])
    #output = combine([1,2,3],3)
    print(output)




