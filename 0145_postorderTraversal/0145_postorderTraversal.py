class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: TreeNode):
    node_list = []
    if root is None:
        return node_list
    postorder(root, node_list)
    return node_list


def postorder(root: TreeNode, node_list: list):
    # 递归退出条件
    if root is None:
        return

    postorder(root.left, node_list)
    postorder(root.right, node_list)
    node_list.append(root.val)


