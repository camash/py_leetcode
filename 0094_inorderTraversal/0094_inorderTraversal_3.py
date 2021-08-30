# morris （将二叉树转化为链表，即每一个node都只可能有右孩子）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    res = []
    while root:
        if root.left:
            # find out predecessor
            predecessor = root.left
            while predecessor.right:
                predecessor = predecessor.right
            # link predecessor to root
            predecessor.right = root
            # set left child of root to None
            temp = root
            root = root.left
            temp.left = None
        else:
            res.append(root.val)
            root = root.right
    return res


if __name__ == '__main__':
    input = TreeNode(2, TreeNode(1,None,TreeNode(8)), TreeNode(3))
    output = inorderTraversal(input)
    print(output)
