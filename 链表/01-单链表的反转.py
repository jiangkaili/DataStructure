# author： 蒋开立
# datetime： 2020/9/4 0:31

def reverse_list(head):
    if head is None:
        return
    if head.next is None:
        return
    p1 = head
    p2 = head.next
    p3 = head.next.next
    while not p3:
        p2.next = p1
        p1 = p2
        p2 = p3
        p3 = p3.next
    p2.next = p1
    return p2
