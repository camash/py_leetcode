class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode):
    node_set = set()
    while headA:
        node_set.add(headA)
        headA = headA.next
    while headB:
        # 比较的实际是地址
        if headB in node_set:
            return headB
        headB = headB.next
    return None


if __name__ == "__main__":
    input1 = ListNode(2)
    input1.next = ListNode(3)
    input2 = ListNode(1)
    input2.next = input1
    output = getIntersectionNode(input1, input2)
    print(output)
