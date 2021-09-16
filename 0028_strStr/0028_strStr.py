# 不能使用双指针，因为haystack其实也要重置
def strStr(haystack, needle):
    if not needle:
        return 0
    i = 0
    n = len(needle)
    h = len(haystack)
    if n > h:
        return -1
    for j in range(h):
        # 相等则继续推进，若为末位则退出
        if haystack[j] == needle[i]:
            if i == n-1:
                return j - i
            else:
                i += 1
        # 不等，则needle位置需重置
        # 若当前点和needle初始位相等，需要使i前进一位
        else:
            if haystack[j] == needle[0]:
                i = 1
            else:
                i = 0

    return -1


if __name__ == '__main__':
    input1 = "mississippi"
    input2 = 'issip'
    output = strStr(input1, input2)
    print(output)