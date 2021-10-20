def insert(intervals: list, newInterval: list):
    intervals.append(newInterval)
    intervals.sort()
    n = len(intervals)
    res = [intervals[0]]
    for i in range(1,n):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(intervals[i][1], res[-1][1])
        else:
            res.append(intervals[i])

    return res


if __name__ == '__main__':
    input1 = [[1,3],[6,9]]
    input2 = [2,5]
    output = insert(input1, input2)
    print(output)


