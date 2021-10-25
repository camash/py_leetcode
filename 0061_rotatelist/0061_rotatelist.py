class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int):
    n = len_listnode(head)
    if n <= 1 or k == 0:
        return head
    step = k % n
    if step == 0:
        return head
    dummy_head = head
    dummy_head_pre = head
    # 最后一位移动几次，位移次数为实际个数-移动次数
    for i in range(1, n-step+1):
        dummy_head = dummy_head.next
        # 最后一步前一步
        if i != n-step:
            dummy_head_pre = dummy_head_pre.next

    # 总结截断
    dummy_head_pre.next = None
    new_head = dummy_head
    # 移动到末尾
    while dummy_head.next:
        dummy_head = dummy_head.next
    dummy_head.next = head

    return new_head


def len_listnode(l: ListNode):
    i = 0
    while l:
        l = l.next
        i += 1
    return i


if __name__ == "__main__":
    input1 = ListNode(1,ListNode(2, ListNode(3)))
    input2 = 2000000000
    result = rotateRight(input1, input2)
    print(result)