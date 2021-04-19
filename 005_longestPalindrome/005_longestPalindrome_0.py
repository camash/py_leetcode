def longestPalindrome(s):
    res = ""
    s_len = len(s)
    for i in range(s_len):
        for j in range((s_len-1),i-1,-1):
            if i == j:
                if len(s[i:j+1]) > len(res):
                    res = s[i:j+1]
            elif s[i:j+1] == s[j:i-1:-1]:
                if len(s[i:j+1]) > len(res):
                    res = s[i:j+1]

    return res


if __name__ == '__main__':
    my_str = "bb"
    result = longestPalindrome(my_str)
    print(result)
