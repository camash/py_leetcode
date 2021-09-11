class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: list, inorder: list):
    # 空值条件
    if not preorder or not inorder:
        return None
    if len(preorder) == 1 or len(inorder) == 1:
        return TreeNode(preorder[0])
    tree = TreeNode(preorder[0])
    root_pos_inorder = inorder.index(preorder[0])
    inorder_left = inorder[:root_pos_inorder]
    inorder_right = inorder[root_pos_inorder+1:]
    # 因为两个数组的长度肯定是相等的
    preorder_left = preorder[1:1+len(inorder_left)]
    preorder_right = preorder[1+len(inorder_left):]
    # 递归
    tree.left = buildTree(preorder_left, inorder_left)
    tree.right = buildTree(preorder_right, inorder_right)

    return tree


if __name__ == "__main__":
    input1 = [3,9,20,15,7]
    input2 = [9,3,15,20,7]
    output = buildTree(input1, input2)
    print(output)
