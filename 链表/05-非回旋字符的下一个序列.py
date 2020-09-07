# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/9/7 1:39 下午
# @File    : 05-非回旋字符的下一个序列.py

alp = "abcdefghijklmnopqrstuvwxyz"


def adjust(num, s):
    i = 0
    tmp = []
    while i < num:
        tmp.append(alp[i])
        i += 1

    tmp_list = []

    for index, value in enumerate(tmp):
        if value == s[-1]:
            tmp_list = tmp[index + 1:]

    str_list = []

    tmp_str = s[:-1]
    for i in tmp_list:
        str_list.append(tmp_str + i)

    tmp_index = []
    Len = len(str_list)
    for index, value in enumerate(str_list):
        if value == value[::-1]:
            tmp_index.append(index)

    if tmp_index:
        tmp_index.sort()
        if tmp_index[-1] < Len:
            res_index = tmp_index[-1]
            return str_list[res_index + 1]


if __name__ == '__main__':
    res = adjust(5, "cba")
    print(res)
