class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root:TreeNode, targetSum):
    if not root:
        return False

    def dfs(node, path_sum, target_sum):
        if not node:
            return False
        if node.left is None and node.right is None:
            path_sum += node.val
            if path_sum == target_sum:
                print(node.val)
                return True
            else:
                return False
        # 分别求左路和右路的路径和，一旦有真值就退出
        if dfs(node.left, path_sum+node.val, targetSum):
            return True

        if dfs(node.right, path_sum+node.val, targetSum):
            return True
        # 没找到最终返回假
        return False

    return dfs(root, 0, targetSum)


if __name__ == '__main__':
    input = TreeNode(5, TreeNode(4, TreeNode(11,TreeNode(7),TreeNode(2))), TreeNode(8,TreeNode(13),TreeNode(4,None,TreeNode(1))))
    output = hasPathSum(input, 22)
    print(output)
