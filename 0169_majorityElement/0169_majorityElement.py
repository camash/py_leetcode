def majorityElement(nums: list):
    element_cnt = {}
    n = 0
    for item in nums:
        n += 1
        if item in element_cnt:
            element_cnt[item] += 1
        else:
            element_cnt[item] = 1

    for x,y in element_cnt.items():
        if y > n/2:
            return x
    return None


if __name__ == '__main__':
    input = [2,2,1,1,1,2]
    output = majorityElement(input)
    print(output)

