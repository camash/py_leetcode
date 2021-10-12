def groupAnagrams(strs: list):
    strs_dict = {}
    for item in strs:
        sorted_item = ''.join(a for a in sorted(item))
        if sorted_item in strs_dict:
            strs_dict[sorted_item].append(item)
        else:
            strs_dict[sorted_item] = [item]

    res = []
    for k, v in strs_dict.items():
        res.append(v)

    return res


if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = groupAnagrams(input)
    print(output)


