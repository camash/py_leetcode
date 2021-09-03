class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(root: TreeNode):
    left_dict = {}
    if root is None:
        return 0

    def dfs(node: TreeNode, level):
        if node is None:
            return
        # 如果是叶子节点则将层级和节点值放入dict中，只有更大的level时才插入
        if node is not None and node.left is None and node.right is None:
            if level not in left_dict.keys():
                left_dict[level] = node.val
        # 然后下进一层，继续看是否有符合的叶子，同时增加层级
        dfs(node.left, level+1)
        dfs(node.right, level+1)

    dfs(root, 0)
    # 找出最大层级对应的节点值
    return left_dict[max(left_dict.keys())]


if __name__ == "__main__":
    input = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5)))
    output = findBottomLeftValue(input)
    print(output)



