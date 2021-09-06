class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode):
    # 使用BST的特征，左子树的所有节点都小于父节点，右子树的所有节点都大于父节点
    def check_branch(node: TreeNode, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True
        # 等于的情况也要排除
        if node.val >= upper or node.val <= lower:
            return False
        return check_branch(node.left, lower, node.val) and check_branch(node.right, node.val, upper)

    return check_branch(root)



if __name__ == "__main__":
    #input = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    input = TreeNode(2, TreeNode(2), TreeNode(2))
    output = isValidBST(input)
    print(output)

