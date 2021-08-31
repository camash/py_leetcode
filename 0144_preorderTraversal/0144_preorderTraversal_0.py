class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode):
    # 进行节点遍历，过程结果放在数组中
    node_list = []
    preorder_traversal(root, node_list)
    return node_list


def preorder_traversal(root:TreeNode, node_list: list):
    # 节点不存在，作为退出条件
    if not root:
       return

    node_list.append(root.val)
    preorder_traversal(root.left, node_list)
    preorder_traversal(root.right, node_list)


if __name__ == '__main__':
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    output = preorderTraversal(input)
    print(output)
