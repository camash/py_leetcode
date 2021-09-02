class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode):
    preorder_list = []
    preorder(root, preorder_list)
    return len(preorder_list)


def preorder(root:TreeNode, res:list):
    if root is None:
        return
    res.append(root.val)
    preorder(root.left, res)
    preorder(root.right, res)



if __name__ == '__main__':
    input = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    output = countNodes(input)
    print(output)



