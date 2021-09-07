class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertBST(root: TreeNode):
    cur_val = 0
    def dfs(root:TreeNode):
        nonlocal cur_val
        if not root:
            return None
        # 直接下钻到最右
        dfs(root.right)
        cur_val += root.val
        root.val = cur_val
        dfs(root.left)
    dfs(root)
    return root


if __name__ == '__main__':
    input = TreeNode(2, TreeNode(1), TreeNode(3))
    output = convertBST(input)
    print("xxx")


