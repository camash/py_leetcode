class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode):
    if root is None:
        return 0
    i = 0
    node = root.left
    # 取最左边的层数
    while node:
        i += 1
        node = node.left
    # 完全二叉树的性质，值的范围在最后一层的左到最右之间
    lmost_count = 2**i
    rmost_count = 2**(i+1) - 1
    # 二分法尽行判断
    while lmost_count < rmost_count:
        mid = (lmost_count + rmost_count)//2+1
        if exists(root, mid):
            lmost_count = mid
        else:
            rmost_count = mid - 1

    return rmost_count


# 判断最后一层节点是否存在
def exists(node:TreeNode, k):
    # 查找路径，1往右，0往左
    path = bin(k)[3:]
    for i in path:
        if i == '1':
            node = node.right
        else:
            node = node.left
    if node:
        return True
    else:
        return False




if __name__ == '__main__':
    input = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    output = countNodes(input)
    print(output)

