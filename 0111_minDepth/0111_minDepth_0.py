class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode):
    depth = 0
    if root is None:
        return depth
    elif root.left is None and root.right is None:
        return 1
    # 单边情况要继续下探，因为该节点还有叶子
    elif root.left and root.right is None:
        depth = 1 + minDepth(root.left)
    elif root.right and root.left is None:
        depth = 1 + minDepth(root.right)
    # 只有两边都可以下探时才用min进行比较
    else:
        depth = 1 + min(minDepth(root.left), minDepth(root.right))
    return depth


if __name__ == '__main__':
    input = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    output = minDepth(input)
    print(output)