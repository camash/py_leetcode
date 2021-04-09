class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_nums(l1:ListNode, l2:ListNode):
    val_l1 = l1.val
    val_l2 = l2.val
    new_l1 = l1.next
    new_l2 = l2.next
    result_list = []
    result_list.append((val_l1 + val_l2)%10)
    promote = int((val_l1 + val_l2)/10)
    while (new_l1 or new_l2 or promote > 0):
        if new_l1:
            val_l1 = new_l1.val
            new_l1 = new_l1.next
        else:
            val_l1 = 0
        if new_l2:
            val_l2 = new_l2.val
            new_l2 = new_l2.next
        else:
            val_l2 = 0
        result_list.append((promote + val_l1 + val_l2)%10)
        promote = int((promote + val_l1 + val_l2)/10)

    print(result_list)
    temp_chain = ListNode(result_list[-1])
    for item in reversed(result_list[:-1]):
        temp_chain = ListNode(item, temp_chain)

    return temp_chain
        
        
        
    
if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    add_two_nums(a,b)
