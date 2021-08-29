# 迭代版更新，用空作为退出，而不是0中的无子节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    res = []
    traversal(root, res)
    return res


def traversal(root, path):
    # 空即为退出条件
    if not root:
        return
    traversal(root.left, path)
    path.append(root.val)
    traversal(root.right, path)


if __name__ == '__main__':
    input = None
    output = inorderTraversal(input)
    print(output)
