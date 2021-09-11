class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node'):
    if not root:
        return None
    # 在当前层处理下一层
    # 下一层的左节点存在，next先取右节点，后取root.next的左节点，然后右节点
    # 并且root.next可能还有next，依次往右边取，应对[1,2,3,4,5,null,6,7,null,null,null,null,8]
    if root.left:
        if root.right:
            root.left.next = root.right
        else:
            tmp_node = root.next
            while tmp_node:
                if tmp_node.left:
                    root.left.next = tmp_node.left
                    break
                elif tmp_node.right:
                    root.left.next = tmp_node.right
                    break
                else:
                    tmp_node = tmp_node.next
    if root.right:
        tmp_node = root.next
        if root.val == 7 and root.right.val==7:
            print(root.right.val)
        while tmp_node:
            if tmp_node.left:
                root.right.next = tmp_node.left
                break
            elif tmp_node.right:
                root.right.next = tmp_node.right
                break
            else:
                tmp_node = tmp_node.next
    # 坑点，右边必须先执行，否则next可能没有维系到
    # 例[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]
    connect(root.right)
    connect(root.left)

    return root


if __name__ == '__main__':
    #input = Node(2, Node(1,Node(0,Node(2)),Node(7,Node(1),Node(0,Node(7)))), Node(3,Node(9),Node(1,Node(8),Node(8))))
    input = Node(5,Node(2,Node(4,Node(7,None,Node(7)),Node(2)),Node(-4,None,Node(-9))),Node(-2,Node(-9,Node(-9)),Node(2,None,Node(3,None,Node(3)))))
    output = connect(input)
    print(output)