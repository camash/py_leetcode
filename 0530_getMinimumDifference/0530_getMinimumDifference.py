class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root: TreeNode):
    ans = float('inf')
    pre = None
    def dfs(root:TreeNode):
        nonlocal pre, ans
        if not root:
            return
        # 递归右子树
        dfs(root.left)
        # 中间点, 左边无节点了，当前节点
        if pre is None:
            pre = root.val
        else:
            ans = min(root.val - pre, ans)
            pre = root.val
        # 递归右子树
        dfs(root.right)
    # 调用
    dfs(root)
    return ans


if __name__ == "__main__":
    input = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    output = getMinimumDifference(input)
    print(output)




