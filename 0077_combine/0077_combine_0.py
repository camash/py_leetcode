def combine(n,k):
    result = []
    # 用回溯法往result里面添加符合条件的组合
    backtracking(n, k, result, 1, [])
    return result


# begin 是树搜索的开始位置，search_list每次查找的临时结果
def backtracking(n, k, result, begin, search_list):
    if len(search_list) == k:
        result.append(search_list.copy())
        return
    for i in range(begin, n+1):
        # 向临时结果中增加一个1..n的元素
        search_list.append(i)
        # 新一轮搜索,新的起点就是i+1
        backtracking(n, k, result, i+1, search_list)
        # 找到之后，需要回到父节点，继续搜索
        search_list.pop()


if __name__ == '__main__':
    output = combine(4,2)
    print(output)



