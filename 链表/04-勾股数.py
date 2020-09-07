# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/9/7 11:53 上午
# @File    : 04-勾股数.py

res = []
new_res = []


def get_zs(i, j, l, k):
    flag = False
    for p in range(2, k):
        if i % p == 0 and j % p == 0 and l % p == 0:
            return False
        else:
            flag = True
    return flag

def get_open(s, k):
    for i in range(k):
        if pow(i, 2) == s:
            return i


def adjust(i, j, k):
    m = pow(i, 2) + pow(j, 2)
    l = None
    if m < k * k:
        l = get_open(m, k)
    if l:
        result = get_zs(i, j, l, k)
        if result is True:
            res.append(sorted([i, j, l]))


def get_res(n, m):
    for i in range(n, m):
        for j in range(n, m):
            adjust(i, j, m)
    for item in res:
        if item not in new_res:
            new_res.append(item)

    return new_res


if __name__ == '__main__':
    s = get_res(1, 20)
    print(s)
