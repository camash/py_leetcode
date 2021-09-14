# 基于recursion递归的尝试
def isValid(s: str):
    if not s:
        return True
    if len(s) < 2:
        return False
    if len(s) == 2:
        if s in ('()', '[]', '{}'):
            return True
        else:
            return False
    pair_dict = {'(': ')', '[': ']', '{': '}'}

    if s[:2] in ('()', '[]', '{}'):
        return isValid(s[2:])
    else:
        # 找出第一个符号匹配的结束位置，去除这两个然后递归
        try:
            paired_pos = s.rindex(pair_dict[s[0]])
        except:
            return False

        return isValid(s[1:paired_pos]) and isValid(s[paired_pos+1:])


if __name__ == '__main__':
    input = "(]"
    input = "(("
    input = "[[[]"
    input = "[({])}"
    input = "()[]{}"
    input = "(([]){})"
    input = "{}{}()[]"
    input = "[({(())}[()])]"
    input = "{}[{}]((){})(){}"


    output = isValid(input)
    print(output)
