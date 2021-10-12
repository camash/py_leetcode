from collections import defaultdict
def groupAnagrams(strs: list):
    str_dict = defaultdict(list)
    for item in strs:
        char_list = [0]*26
        for c in item:
            char_list[ord(c) - ord("a")] += 1
        # list is unhashable
        str_dict[tuple(char_list)].append(item)

    return list(str_dict.values())


if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = groupAnagrams(input)
    print(output)



