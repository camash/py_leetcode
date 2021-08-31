def isInterleave(s1, s2, s3):
    # 先满足最后一位
    forward_state = basic_check(s1, s2, s3)
    reverse_state = basic_check(s1[::-1], s2[::-1], s3[::-1])

    return forward_state or reverse_state


def basic_check(s1, s2, s3):
    for item in s3:
        if s1 and item == s1[0]:
            s1 = s1[1:]
        elif s2 and item == s2[0]:
            s2 = s2[1:]
        else:
            return False
    return True



if __name__ == '__main__':

    s1 = "a"
    s2 = "b"
    s3 = "a"
    s1 = "aabc"
    s2 = "abad"
    s3 = "aabadabc"

    print(isInterleave(s1,s2,s3))

