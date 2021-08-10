def lengthOfLongestSubstring(s):
    left = -1
    val_dict = {}
    max_len = 0
    for right, item in enumerate(s):
        # 需要排除后面再次出现left左边的字符，如"tmmzuxt"
        if item in val_dict : #and left < val_dict[item]:
            left = val_dict[item]
            val_dict[item] = right
        else:
            val_dict[item] = right
            max_len = max(max_len, right - left)

    #print(val_dict)
    return max_len

if __name__ == "__main__":
    str = "tmmzuxtz"
    result = lengthOfLongestSubstring(str)
    print(result)

