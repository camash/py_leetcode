class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: TreeNode):
    if not root:
        return []
    cur_val_list = [root.val]
    res_list = [cur_val_list]
    cur_node_list = []
    if root.left: cur_node_list.append(root.left)
    if root.right: cur_node_list.append(root.right)
    # 从第二层开始循环
    while cur_node_list:
        tmp_node_list = []
        cur_val_list = []
        # 循环当前层的每一个节点
        for node in cur_node_list:
            if node:cur_val_list.append(node.val)
            if node.left: tmp_node_list.append(node.left)
            if node.right: tmp_node_list.append(node.right)
        res_list.append(cur_val_list)
        cur_node_list = tmp_node_list

    return res_list[::-1]


if __name__ == "__main__":
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    output = levelOrderBottom(input)
    print(output)