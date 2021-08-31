class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: TreeNode):
    node_list = []
    if root is None:
        return node_list
    # 初始化栈和遍历指针
    stack = []
    cur = root
    while cur or stack:
        while cur:
            # 当前节点压栈
            stack.append(cur)
            cur = cur.left
        # 左子树遍历完成，先把左边节点放入结果集
        node_list.append(cur.val)
        cur = stack.pop()
        cur = cur.right

