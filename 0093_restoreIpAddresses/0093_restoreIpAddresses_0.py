def restoreIpAddresses(s):
    res = []
    for i in range(1,4):
        for j in range(1, 4):
            for k in range(1, 4):
                for l in range(1, 4):
                    if i + j + k + l == len(s):
                        s1 = s[0:i]
                        s2 = s[i:i+j]
                        s3 = s[i+j:i+j+l]
                        s4 = s[i+j+l:]

                        if check(s1) and check(s2) and check(s3) and check(s4):
                            ip_str = s1 + '.' + s2 + '.' + s3 + '.' + s4
                            res.append(ip_str)

    return res


def check(s):
    if int(s) < 256:
        if (s[0:1] != '0' and int(s)>0) or s == '0':
            return True

    return False


if __name__ == '__main__':
    output = restoreIpAddresses('1111')
    print(output)

