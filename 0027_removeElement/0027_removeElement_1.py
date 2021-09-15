# 使用pop函数, 可以保证地址不变
def removeElement(self, nums: List[int], val: int) -> int:
    print(hex(id(nums)))
    n = len(nums)
    while val in nums:
        # 中间移到后面，则前面要补数
        nums.pop(nums.index(val))
    print(hex(id(nums)))
    return len(nums)