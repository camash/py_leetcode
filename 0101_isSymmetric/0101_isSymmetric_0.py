class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSysmmetric(root: TreeNode):
    if root is None:
        return True
    res = compare_LR(root.left, root.right)
    return res


def compare_LR(l_node: TreeNode, r_node: TreeNode):
    # 退出条件1，都为空
    if l_node is None and r_node is None:
        return True
    # 退出条件2,3，一个节点空，一个节点部位空
    elif l_node is None and r_node:
        return False
    elif l_node and r_node is None:
        return False
    # 递归操作，返回根结点相等，且左边的左子树=右边的右子树，左边的右子树=右边的左子树
    else:
        return (l_node.val == r_node.val) \
               and compare_LR(l_node.left, r_node.right) \
               and compare_LR(l_node.right, r_node.left)


if __name__ == '__main__':
    input = TreeNode(1, TreeNode(2), TreeNode(3))
    output = isSysmmetric(input)
    print(output)
