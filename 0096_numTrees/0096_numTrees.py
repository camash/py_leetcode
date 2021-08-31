class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_trees(n):
    # G保存n个节点的BST的个数，初始值都为0
    # 数组有记忆功能，其实使用的是迭代法向前计算G[n]的值，过程用到G[i<n]的结果
    G = [0]*(n+1)
    G[0] = 1
    G[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] = G[i] + G[j-1]*G[i-j]

    return G[n]


if __name__ == "__main__":
    output = num_trees(2)
    print(output)