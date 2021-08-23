# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1,l2):
    final_list = ListNode(-200)
    dummy = final_list
    while l1 and l2:
        if l1.val < l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        # 这个指针的推进非常重要，单纯的next只会让数据在原位置不断的更新。
        dummy = dummy.next

    if l1 is not None:
        dummy.next = l1
    else:
        dummy.next = l2

    return final_list.next


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    res_list = mergeTwoLists(list1, list2)
    while res_list:
        print(res_list.val)
        res_list = res_list.next
