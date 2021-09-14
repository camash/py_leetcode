# 总是在内层有两个相连，将其剔除
def isValid(s: str):
    pair_dict = {'(': ')', '[': ']', '{': '}'}
    n = len(s)
    # 若没事去除两个元素，则最多循环n//2次
    for j in range(n//2):
        for i in range(len(s)-1):
            # 如果开始即为后半个，则必然出错
            if s[i] not in pair_dict.keys():
                return False
            # 找到一个相邻就删除之，再从外层循环
            if pair_dict[s[i]] == s[i+1]:
                if i+2 > n - 1:
                    s = s[:i]
                else:
                    s = s[:i] + s[i+2:]
                break
    if s:
        return False
    else:
        return True


if __name__ == '__main__':
    input = "(]"
    input = "(("
    #input = "[[[]"
    #input = "[({])}"
    #input = "()[]{}"
    #input = "(([]){})"
    #input = "{}{}()[]"
    #input = "[({(())}[()])]"
    #input = "{}[{}]((){})(){}"
    input = "([)]"


    output = isValid(input)
    print(output)


