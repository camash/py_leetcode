class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right


def searchBST(root: TreeNode, val: int):
    if not root or not val:
        return None
    node = root
    while node:
        if node.val == val:
            return node
        elif node.val > val:
            node = node.left
        else:
            node = node.right

    return None


