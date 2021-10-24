def getPermutation(n: int, k: int):
    # 阶乘表
    fact = [1]
    if n > 1:
        for i in range(2,n+1):
            fact.append(fact[-1]*i)
    # 备选清单
    seed = [str(i) for i in range(1,n+1)]
    res = ""
    # 适应数组从零开始计数
    k = k -1
    for i in range(n-1,0,-1):
        # 与下一层的阶乘比较说明经过几轮这样的阶乘，即为第一个系数
        pos = k // fact[i-1]
        k = k % fact[i-1]
        # 从备选清单中取出
        res += seed.pop(pos)

    res += seed[-1]

    return res


if __name__ == "__main__":
    input1 = 9
    input2 = 296662
    output = getPermutation(input1, input2)
    print(output)


