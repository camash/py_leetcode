def merge(intervals: list):
    intervals.sort()
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        # 后段的初始位在前段的范围内，则重置结束位
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        # 否则，追加该段
        else:
            res.append(intervals[i])

    return res


if __name__ == '__main__':
    input = [[1,4],[4,5]]
    output = merge(input)
    print(output)

