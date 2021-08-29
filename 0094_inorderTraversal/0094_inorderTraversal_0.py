class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    res = []
    # 非空判断
    if not root:
        inorder(root, res)
    return res


# 参照0077的方式利用数组变量保存遍历过程中的所有结果
def inorder(root: TreeNode, path: list):
    if root.left is None and root.right is None:
        path.append(root.val)
        return
    if root.left:
        inorder(root.left, path)
        # 遍历完成左边后，把根结点加入
    path.append(root.val)
    if root.right:
        inorder(root.right, path)






if __name__ == '__main__':
    input = TreeNode()
    output = inorderTraversal(input)
    print(output)