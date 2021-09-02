class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: TreeNode):
    i = 0
    res = 0
    # 提前赋值，避免控制的情况
    prev = root
    # 取最右边的层数
    while root:
        prev = root
        res += pow(2,i)
        i += 1
        root = root.right
    # 退出时两种情况, 有左子节点，则多一层减去1
    if prev.left:
        res += pow(2,i) - 1
    return res


if __name__ == '__main__':
    input = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    output = countNodes(input)
    print(output)

