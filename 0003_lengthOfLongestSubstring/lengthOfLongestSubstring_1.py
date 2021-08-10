def lengthOfLongestSubstring(s):
    cur_len = 0
    sub_list = []
    for item in s:
        if item not in sub_list:
            sub_list.append(item)
            print(sub_list)
            if len(sub_list) >= cur_len:
                cur_len = len(sub_list)
        else:
            dup_idx = sub_list.index(item)
            sub_list = sub_list[dup_idx+1:]
            sub_list.append(item)
            print(sub_list)

    #print(sub_list)
    return cur_len


if __name__ == "__main__":
    str = "abcabcbb"
    result = lengthOfLongestSubstring(str)
    print(result)
