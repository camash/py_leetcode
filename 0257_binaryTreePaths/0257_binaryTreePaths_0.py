class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: TreeNode):
    def construct_paths(root:TreeNode, path):
        if root is None:
            return
        else:
            path = path + str(root.val)
            if root.left is None and root.right is None:
                paths.append(path)
            else:
                path += '->'
                construct_paths(root.left, path)
                construct_paths(root.right, path)



    paths = []
    construct_paths(root, '')
    return paths


if __name__ == '__main__':
    input = TreeNode(None)
    output = binaryTreePaths(input)
    print(output)