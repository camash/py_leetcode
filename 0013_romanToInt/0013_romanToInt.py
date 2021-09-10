def romanToInt(s: str):
    res = 0
    while s:
        if s[-1] == 'X':
            if len(s)>1 and s[-2] == 'I':
                res += 9
                s = s[:-2]
            else:
                res += 10
                s = s[:-1]
        elif s[-1] == 'V':
            if len(s)>1 and s[-2] == 'I':
                res += 4
                s = s[:-2]
            else:
                res += 5
                s = s[:-1]
        elif s[-1] == 'C':
            if len(s)>1 and s[-2] == 'X':
                res += 90
                s = s[:-2]
            else:
                res += 100
                s = s[:-1]
        elif s[-1] == 'L':
            if len(s)>1 and s[-2] == 'X':
                res += 40
                s = s[:-2]
            else:
                res += 50
                s = s[:-1]
        elif s[-1] == 'M':
            if len(s)>1 and s[-2] == 'C':
                res += 900
                s = s[:-2]
            else:
                res += 1000
                s = s[:-1]
        elif s[-1] == 'D':
            if len(s)>1 and s[-2] == 'C':
                res += 400
                s = s[:-2]
            else:
                res += 500
                s = s[:-1]
        else:
            res += 1
            s = s[:-1]

    return res


if __name__ == "__main__":
    input = 'LVIII'
    output = romanToInt(input)
    print(output)






