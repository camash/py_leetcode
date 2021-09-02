#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if root is None:
        return True
    # 只有根
    elif height(root) == 1:
        return True
    # 双层
    elif height(root) == 2:
        return True
    # 按子节点递归
    else:
        return (isBalanced(root.left) and isBalanced(root.right)
               and abs(height(root.left) - height(root.right))<2)


def height(node: TreeNode):
    if node is None:
        return 0
    return 1+max(height(node.left), height(node.right))


if __name__ == "__main__":
    input = TreeNode(1, TreeNode(2,TreeNode(4,TreeNode(6))), TreeNode(3))
    output = isBalanced(input)
    print(output)