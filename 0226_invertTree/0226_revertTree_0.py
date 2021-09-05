class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode):
    if root is None:
        return root
    temp_branch = root.left
    root.left = invertTree(root.right)
    root.right = invertTree(temp_branch)

    return root


if __name__ == '__main__':
    input = TreeNode(1, TreeNode(2, TreeNode(21),TreeNode(22)), TreeNode(3, TreeNode(31)))
    output = invertTree(input)
    print("xxx")

