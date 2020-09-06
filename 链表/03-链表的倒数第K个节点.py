# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/9/6 11:45 下午
# @File    : 03-链表的倒数第K个节点.py


class Solution:
    def find_kth_to_tail(self, head, k):
        first = head
        second = head
        for i in range(k):
            if first is None:
                return
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        return second
