# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/9/7 12:43 下午
# @File    : 05-寻找<[{的数量.py


import re


def adjust(s, num):
    l = len(s)
    if num == 1:
        index = 0
        count = 0
        tmp = 0
        while index < l:
            if s[index] == '<':
                tmp += 1
            if s[index] == '>':
                count += 1
            index += 1
        if tmp == count:
            return tmp
        else:
            return count

    elif num == 2:
        index = 0
        count = 0
        tmp = 0
        while index < l:
            if s[index] == '[':
                tmp += 1
            if s[index] == ']':
                count += 1
            index += 1
        if tmp == count:
            return tmp
        else:
            return count
    elif num == 3:
        index = 0
        count = 0
        tmp = 0
        while index < l:
            if s[index] == '{':
                tmp += 1
            if s[index] == '}':
                count += 1
            index += 1
        if tmp == count:
            return tmp
        else:
            return count


def get_count(res):
    count1 = adjust(res, 1)
    count2 = adjust(res, 2)
    count3 = adjust(res, 3)
    return count1 + count2 + count3


if __name__ == '__main__':
    s = "<<abc>ss[012]{vv}>"
    res = get_count(s)
    print(res)
