class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
    if not root:
        return None
    if root == p:
        return root
    if root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    # 左右子树都不含有p，q
    if not left and not right:
        return None
    # p,q分别在左右子树
    if left and right:
        return root
    # 左子树中未找到，返回right （可能为其中一个节点，可能为两个节点的最近公共祖先节点）
    if not left:
        return right
    if not right:
        return left

# OJ中比较的是树的根结点值
if __name__ == '__main__':
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    p = input.left
    q = input.right
    output = lowestCommonAncestor(input, p, q)
    print(output)
