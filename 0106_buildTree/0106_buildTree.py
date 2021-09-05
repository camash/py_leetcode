class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder, postorder):
    tree = TreeNode(None)
    # 空数
    if not postorder:
        return
    else:
        mid = postorder[-1]
        tree.val = mid
        # 找左边和右边的inorder节点数组，使用index的前提是没有重复的元素
        mid_pos_inorder = inorder.index(mid)
        left_inorder = inorder[:mid_pos_inorder]
        right_inorder = inorder[mid_pos_inorder+1:]
        # 找左边和右边的postorder节点数组
        left_postorder = postorder[:mid_pos_inorder]
        right_postorder = postorder[mid_pos_inorder:-1]
        # 通过递归继续对左右树进行构造
        tree.left = buildTree(left_inorder, left_postorder)
        tree.right = buildTree(right_inorder, right_postorder)

    return tree


if __name__ == '__main__':
    input1 = [9,3,15,20,7]
    input2 = [9,15,7,20,3]
    output = buildTree(input1, input2)
    print("xxx")



