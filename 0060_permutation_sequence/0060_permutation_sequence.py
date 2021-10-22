def getPermutation(n: int, k: int):

    # 候选数组alist, 排列长度m, 已有元素blist, 排列清单plsit
    def backTracking(alist: list, m: int, blist: list, plist: list):
        if len(blist) == m:
            plist.append(blist.copy())
            return
        for i in range(len(alist)):
            if alist[i] in blist:
                continue
            blist.append(alist[i])
            backTracking(alist, m, blist, plist)
            blist.pop()

    plist = []
    alist = [i+1 for i in range(n)]
    backTracking(alist, n, [], plist)
    return "".join([str(i) for i in plist[k-1]])


if __name__ == "__main__":
    input1 = 3
    input2 = 2
    output = getPermutation(input1, input2)
    print(output)