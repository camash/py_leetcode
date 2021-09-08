class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: TreeNode, val: int):
    # 根据题意val不为空值
    if not root:
        return TreeNode(val)
    node = root
    direction = 'left'
    while node:
        # 记录遍历到的位置
        pre = node
        if val < node.val:
            node = node.left
            direction = 'left'
        else:
            node = node.right
            direction = 'right'

    if direction == 'left':
        pre.left = TreeNode(val)
    else:
        pre.right = TreeNode(val)

    return root


if __name__ == '__main__':
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    output = insertIntoBST(input, 4)
    print(output)