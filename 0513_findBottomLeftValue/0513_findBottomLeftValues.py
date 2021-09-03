class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(root: TreeNode):
    left_dict = {}
    if root is None:
        return 0

    def dfs(node: TreeNode, level):
        if node is None:
            return
        # 如果是左子节点则将层级和节点值放入dict中，其中level需要在当前层级的基础上加1
        if node.left is not None and node.left.left is None and node.left.right is None:
            if level+1 not in left_dict.keys():
                left_dict[level+1] = node.left.val
        # 然后下进一层，继续看是否有符合的左节点，同时增加层级
        dfs(node.left, level+1)
        dfs(node.right, level+1)

    dfs(root, 0)
    print(left_dict)


if __name__ == "__main__":
    input = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5)))
    findBottomLeftValue(input)
    #output = (input)
    #print(output)



