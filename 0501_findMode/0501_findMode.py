class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: TreeNode):
    pre = None
    val_cnt = {}
    def dfs(root: TreeNode):
        nonlocal pre
        if not root:
            return None
        dfs(root.left)
        if pre is None:
            val_cnt[root.val] = 1
            pre = root.val
        else:
            if pre == root.val:
                val_cnt[root.val] += 1
            else:
                val_cnt[root.val] = 1
            pre = root.val
        dfs(root.right)
    dfs(root)
    max_occur = max(val_cnt.values())

    return [item for item, count in val_cnt.items() if count == max_occur]



if __name__ == "__main__":
    input = TreeNode(4, TreeNode(4), TreeNode(6, TreeNode(6)))
    output = findMode(input)
    print(output)






