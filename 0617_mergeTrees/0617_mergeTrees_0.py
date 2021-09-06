class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: TreeNode, root2: TreeNode):
    tree = TreeNode()
    # 退出条件，即root1,root2都为空节点
    if (not root1) and (not root2):
        return
    else:
        # 特别要对于空节点进行处理
        tree.val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        tree.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        tree.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

    return tree


if __name__ == "__main__":
    input1 = TreeNode(1, TreeNode(2,None,TreeNode(10)), TreeNode(3))
    input2 = TreeNode(4, TreeNode(5))
    output = mergeTrees(input1, input2)
    print("xxx")

