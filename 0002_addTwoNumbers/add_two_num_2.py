class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_nums(l1:ListNode, l2:ListNode):
    dummy_head = ListNode()
    promote = 0
    p = dummy_head
    #print(id(p))
    while (l1 or l2 or promote>0):
        val1 = val2 = 0
        if l1:
            val1 = l1.val
            l1 = l1.next

        if l2:
           val2 = l2.val
           l2 = l2.next

        promote, local = divmod(val1+val2+promote, 10)
        #print(id(p))
        #print(local)
        p.next = ListNode(local)
        # p 相当于链上的指针
        p = p.next

    # 验证
    #print("==========")
    #print(id(dummy_head))
    #print(id(dummy_head.next))
    #print(id(dummy_head.next.next))
    #print(id(dummy_head.next.next.next))

    return dummy_head.next
        
        
        
    
if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    add_two_nums(a,b)
