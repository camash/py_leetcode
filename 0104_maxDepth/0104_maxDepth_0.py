class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode):
    depth = 0
    if root is None:
        return depth
    depth = 1 + max(maxDepth(root.left), maxDepth(root.right))
    return depth


if __name__ == '__main__':
    input = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    output = maxDepth(input)
    print(output)