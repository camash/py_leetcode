def searchRange(nums: list, target: int):
    a = -1
    b = -1
    try:
        a = nums.index(target)
    except Exception as e:
        print(e)

    try:
        b = len(nums) - nums[-1::-1].index(target) - 1
    except Exception as e:
        print(e)

    return [a,b]


if __name__ == '__main__':
    input1 = [5,7,7,8,8,10]
    input2 = 8
    output = searchRange(input1, input2)
    print(output)


