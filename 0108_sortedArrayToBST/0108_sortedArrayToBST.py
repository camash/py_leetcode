class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: list):
    if not nums:
        return None
    len_nums = len(nums)
    mid_pos = len_nums // 2
    # 中间节点
    root = TreeNode(nums[mid_pos])
    # 左子树存在
    if nums[0:mid_pos]:
        root.left = sortedArrayToBST(nums[0:mid_pos])
    # 右子树存在
    if mid_pos < len_nums and nums[mid_pos+1:]:
        root.right = sortedArrayToBST(nums[mid_pos+1:])

    return root


if __name__ == "__main__":
    input = [1,2,3]
    output = sortedArrayToBST(input)
    print(output)