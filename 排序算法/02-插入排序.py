# author： 蒋开立
# datetime： 2020/9/3 23:28

def insert_sort(nums):
    for i in range(1, len(nums)):
        value = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > value:
                nums[j + 1] = nums[j]
            else:
                break
            j -= 1
        nums[j+1] = value
    return nums
