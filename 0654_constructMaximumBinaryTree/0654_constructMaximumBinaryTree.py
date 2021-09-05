class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    tree = TreeNode()
    if not nums:
        return
    else:
        mid = max(nums)
        tree.val = mid
        # 使用index的前提不含重复元素
        mid_pos = nums.index(mid)
        left_nums = nums[:mid_pos]
        right_nums = nums[mid_pos+1:]
        tree.left = constructMaximumBinaryTree(left_nums)
        tree.right = constructMaximumBinaryTree(right_nums)

    return tree


if __name__ == '__main__':
    input = [1,3,2]
    output = constructMaximumBinaryTree(input)
    print("xxx")





