def romanToInt(s: str):
    res = 0
    while s:
        if s[-1] == 'X':
            if s[-2] == 'I':
                res += 9
                s = s[:-2]
            else:
                res += 10
                s = s[:-1]
        elif s[-1] == 'V':
            if s[-2] == 'I':
                res += 4
                s = s[:-2]
            else:
                res += 5
                s = s[:-1]
        elif s[-1] == 'C':
            if s[-2] == 'X':
                res += 90
                s = s[:-2]
            else:
                res += 100
                s = s[:-1]
        elif s[-1] == 'L':
            if s[-2] == 'X':
                res += 40
                s = s[:-2]
            else:
                res += 50
                s = s[:-1]
        elif s[-1] == 'M':
            if s[-2] == 'C':
                res += 900
                s = s[:-2]
            else:
                res += 1000
                s = s[:-1]
        elif s[-1] == 'D':
            if s[-2] == 'C':
                res += 400
                s = s[:-2]
            else:
                res += 500
                s = s[:-1]
        else:
            res += 1






