def isValid(s: str):
    pair_dict = {}
    cnt_dict = {'(':0,')':0,'[':0,']':0,'{':0,'}':0}
    n = len(s)
    if n % 2 != 0:
        return False
    for i in range(n):
        cnt_dict[s[i]] += 1
        if s[i] == ')':
            # 距离在偶数差
            if '(' in pair_dict.keys() and ((i - pair_dict['(']-1) % 2 == 0):
                del pair_dict['(']
            else:
                return False
        elif s[i] == ']':
            # 距离在偶数差
            if '[' in pair_dict.keys() and ((i - pair_dict['[']-1) % 2 == 0):
                del pair_dict['[']
            else:
                return False
        elif s[i] == '}':
            # 距离在偶数差
            if '{' in pair_dict.keys() and ((i - pair_dict['{']-1) % 2 == 0):
                del pair_dict['{']
            else:
                return False
        else:
            pair_dict[s[i]] = i

    # 成对出现的情况最后肯定是清空的
    if len(pair_dict) == 0 and cnt_dict['('] == cnt_dict[')'] and cnt_dict['['] == cnt_dict[']'] and cnt_dict['{'] == cnt_dict['}']:
        return True
    else:
        return False


if __name__ == '__main__':
    input = "(]"
    input = "(("
    input = "[[[]"
    input = "[({])}"
    output = isValid(input)
    print(output)
