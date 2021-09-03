class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root:TreeNode):
    # 用lambda表达式验证是否为叶子节点
    isLeafNode = lambda node: not node.left and not node.right

    def dfs(node: TreeNode):
        ans = 0
        if node.left:
            # 左子节点存在，判断是否为叶子，是则加上左子节点的值，否则继续迭代左子树
            ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
        if node.right:
            # 右子节点存在，则从右子树查找左叶子
            ans += dfs(node.right)
        return ans

    return dfs(root) if root else 0


if __name__ == "__main__":
    input = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5)))
    output = sumOfLeftLeaves(input)
    print(output)


