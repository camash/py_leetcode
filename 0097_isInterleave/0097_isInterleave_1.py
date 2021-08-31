def isInterleave(s1, s2, s3):
    len_1 = len(s1)
    len_2 = len(s2)
    len_3 = len(s3)
    if len_3 != len_1 + len_2:
        return False
    # 动态规划矩阵初始化 行 1-len1 代表s1的字母， 列1-len2代表s2的字母
    # 含义为s3的前i+j个字母能否由s1的前i个字母和s2的前j个字母组成
    dp = [[False]*(len_2+1) for i in range(len_1+1)]
    # 初始化
    dp[0][0] = True
    # 初始化首列, 转换为上面的字母都对上，第i个字母也相等，i-1是因为字符串中从0开始计数
    # 场景就是s2为空的情况
    for i in range(1, len_1+1):
        dp[i][0] = dp[i-1][0] and (s3[i-1] == s1[i-1])
    # 初始化首行，即s1为空的情况
    for j in range(1, len_2+1):
        dp[0][j] = dp[0][j-1] and (s3[j-1] == s2[j-1])

    # 表示i+j-1个s3字母已经匹配的两种情况
    for i in range(1, len_1+1):
        for j in range(1, len_2+1):
            dp[i][j] = (dp[i][j-1] and s3[i+j-1] == s2[j-1]) or (dp[i-1][j] and s3[i+j-1] == s1[i-1])

    return dp[-1][-1]


if __name__ == '__main__':

    s1 = "aabc"
    s2 = "abad"
    s3 = "aabadabc"

    print(isInterleave(s1,s2,s3))

