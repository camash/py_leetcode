class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removedNthFromEnd(head: ListNode, n: int):
    node_dict = {}
    i = 0
    while head:
        node_dict[i] = head
        head = head.next
        i += 1

    remove_node = i - n
    if remove_node == 0:
        return node_dict[0].next
    elif remove_node > 0:
        tmp_node = node_dict[0]
        for i in range(remove_node-1):
            tmp_node = tmp_node.next
        tmp_node.next = node_dict[remove_node].next
        return node_dict[0]
    else:
        return None


if __name__ == '__main__':
    #input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    input = ListNode(1,ListNode(2))
    output = removedNthFromEnd(input, 1)
    print(output)




