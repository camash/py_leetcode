class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: TreeNode, low: int, high: int):
    tree = trimLeft(root, low)
    return trimRight(tree, high)


# 左边界
def trimLeft(root: TreeNode, low: int):
    if not root:
        return root
    if root.val == low:
        root.left = None
    # 如果root值小于low，那么root极其左边都可以去除
    if root.val < low:
        return trimLeft(root.right, low)
    # 如果root值大于low，继续对左子树进行裁剪
    if root.val > low:
        root.left = trimLeft(root.left, low)

    return root


# 右边界
def trimRight(root: TreeNode, high: int):
    if not root:
        return root
    if root.val == high:
        root.right = None
    # 当前值大于high，直接去除
    if root.val > high:
        return trimRight(root.left, high)
    if root.val < high:
        root.right = trimRight(root.right, high)

    return root


if __name__ == "__main__":
    input = TreeNode(1, TreeNode(0), TreeNode(2))
    output = trimBST(input, 1, 2)
    print(output)
