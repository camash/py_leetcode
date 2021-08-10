def lengthOfLongestSubstring(s):
    left = -1
    val_dict = {}
    max_len = 0
    for right, item in enumerate(s):
        # 如果出现重复值，即将left位置移动到重复值上一次出现的位置
        if item in val_dict:
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

