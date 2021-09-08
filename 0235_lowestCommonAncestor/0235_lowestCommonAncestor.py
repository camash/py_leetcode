class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
    # 参考236，利用BST的在于是否决定往左右子树进行搜索
    if not root:
        return None
    if root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q) if p.val < root.val or q.val < root.val else None
    right = lowestCommonAncestor(root.right, p, q) if p.val > root.val or q.val > root.val else None
    if not left and not right:
        return None
    if not left:
        return right
    if not right:
        return left
    return root

