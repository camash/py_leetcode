class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: TreeNode, key: int):
    if not root:
        return root
    # 递归
    if root.val == key:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # 都不为空，取左子树最右边嫁接右子树，并返回左子树
        else:
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            return root.left

    # 从左侧删除
    if root.val > key:
        root.left = deleteNode(root.left, key)
    if root.val < key:
        root.right = deleteNode(root.right, key)

    return root



if __name__ == "__main__":
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    output = deleteNode(input, 2)
    print(output)






