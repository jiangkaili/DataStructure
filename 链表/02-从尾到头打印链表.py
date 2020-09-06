# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/9/6 11:07 下午
# @File    : 02-从尾到头打印链表.py


class Solution:
    def printListFromTailToHead(self, listNode):
        ret = []
        p = listNode
        while p:
            ret.insert(0, p)
            p = p.next
        return ret
