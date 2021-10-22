def getPermutation(n: int, k: int):

    # 候选数组alist, 排列长度m, 已有元素blist, 排列清单plsit, 目标个数k
    def backTracking(alist: list, m: int, blist: list, plist: list, k: int):
        if len(blist) == m:
            plist.append(blist.copy())
            return
        # 可以实现一路返回
        if len(plist) == k:
            return
        else:
            for i in range(len(alist)):
                if alist[i] in blist:
                    continue
                blist.append(alist[i])
                backTracking(alist, m, blist, plist, k)
                blist.pop()

    plist = []
    alist = [i+1 for i in range(n)]
    backTracking(alist, n, [], plist, k)
    #print(plist)
    return "".join([str(i) for i in plist[k-1]])


if __name__ == "__main__":
    input1 = 9
    input2 = 296662
    output = getPermutation(input1, input2)
    print(output)