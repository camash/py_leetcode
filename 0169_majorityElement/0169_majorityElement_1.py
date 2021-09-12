def majorityElement(nums: list):
    counts = 0
    major = None
    for num in nums:
        if counts == 0:
            major = num
        counts += 1 if major == num else -1

    return major


if __name__ == '__main__':
    input = [2,2,1,1,1,2,2]
    output = majorityElement(input)
    print(output)

