# author： 蒋开立
# datetime： 2020/9/3 23:39

def quick_sort(arr, start, end):
    p1, p2 = start, end
    if p1 >= p2:
        return
    flag = arr[p1]
    while p1 < p2:
        while arr[p2] >= flag and p1 < p2:
            p2 -= 1
        arr[p2] = arr[p1]
        while arr[p1] < flag and p1 < p2:
            p1 += 1
        arr[p1] = flag
        quick_sort(arr, start, p1 - 1)
        quick_sort(arr, p1 + 1, end)
