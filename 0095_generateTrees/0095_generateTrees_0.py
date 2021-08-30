class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n):
    if n:
        return generate_trees(1,n)
    else:
        return []

# 重载生成函数
def generate_trees(start, end):
    # 退出条件
    if start > end:
        return [None,]

    allTrees = []
    # 从范围中遍历所有的根结点
    for i in range(start, end+1):
        leftTrees = generate_trees(start, i-1)
        rightTrees = generate_trees(i+1, end)

        # 从左子树的集合中选出一棵，从右子树的集合中选出一棵，与根节点进行组合
        for l_tree in leftTrees:
            for r_tree in rightTrees:
                currTree = TreeNode(i)
                currTree.left = l_tree
                currTree.right = r_tree
                allTrees.append(currTree)
    return allTrees


if __name__ == "__main__":
    output = generateTrees(3)
    print(output)






