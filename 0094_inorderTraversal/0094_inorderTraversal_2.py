# 使用迭代法，中序 左->中->右
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    res = []
    stack = []
    # 记录当前所在节点
    cur = root
    while cur or stack:
        # 判断是否为节点（有值），是节点则压栈
        if cur:
            stack.append(cur) # 节点压栈
            cur = cur.left  # 继续向左推进
        else:
            cur = stack.pop() # 取回上次成功压入的节点，当前路径上可得的中间最底点
            res.append(cur.val) # 将该路径上的最底点放入结果
            cur = cur.right

    return res


if __name__ == '__main__':
    input = TreeNode(2, TreeNode(1,None,TreeNode(8)), TreeNode(3))
    output = inorderTraversal(input)
    print(output)

