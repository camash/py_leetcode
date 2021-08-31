class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode):
    res = []
    if not root:
        return res
    # 树的节点栈
    stack = []
    cur = root
    while cur or stack:
        # 对树进行遍历
        while cur:
            res.append(cur.val)
            # 当前节点压栈，用于后面处理右子树
            stack.append(cur)
            # 继续向左子树前进
            cur = cur.left
        # 支路遍历完成后，出栈当前节点的右子树
        cur = stack.pop()
        cur = cur.right

    return res


if __name__ == '__main__':
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    output = preorderTraversal(input)
    print(output)
