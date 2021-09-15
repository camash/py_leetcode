class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode):
    if not head:
        return
    # 单节点
    if not head.next:
        return head
    if not head.next.next:
        return ListNode(head.next.val, ListNode(head.val))
    right_part = head.next.next
    left_part = ListNode(head.next.val, ListNode(head.val))
    left_part.next.next = swapPairs(right_part)
    return left_part


if __name__ == '__main__':
    input = ListNode(1,ListNode(2, ListNode(3)))
    output = swapPairs(input)
    print(output)
