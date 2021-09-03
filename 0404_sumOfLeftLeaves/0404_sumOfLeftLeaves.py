class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: TreeNode):
    if not root:
        return 0
    res,lmost = 0,0
    # 从当前节点看有没有左叶子
    if root.left is not None and root.left.left is None and root.left.right is None:
        lmost = root.left.val
    lpart = sumOfLeftLeaves(root.left)
    rpart = sumOfLeftLeaves(root.right)
    res = lmost + lpart + rpart
    return res




if __name__ == "__main__":
    input = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5)))
    output = sumOfLeftLeaves(input)
    print(output)



