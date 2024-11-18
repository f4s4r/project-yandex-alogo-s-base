rand_list = [-1, -2, 1, 2, 3, 4, 5, 6, 7, 8]
def bin_search(list_, num, first_el_id=0):
    if num == list_[0]:
        return first_el_id
    cur_len = len(list_)
    left = list_[:cur_len // 2]
    right = list_[cur_len // 2:]
    if len(right) > 0 and num >= right[0]:
        return bin_search(right, num, first_el_id=first_el_id + cur_len // 2)
    elif len(left) > 0:
        return bin_search(left, num, first_el_id=first_el_id)

def bin_s(arr, num):
    cur_len = len(arr)
    res = 0
    while cur_len > 1:
        left = arr[:cur_len // 2]
        right = arr[cur_len // 2:]
        if num >= right[0]:
            arr = right
            cur_len = len(right)
            res += len(left)
        else:
            arr = left
            cur_len = len(left)
    else:
        return res
