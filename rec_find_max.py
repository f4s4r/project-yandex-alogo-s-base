def rec_find_max(arr, cur_max=0):
    cur_len = len(arr)
    if cur_len == 1:
        if arr[0] > cur_max:
            return arr[0]
        else:
            return cur_max
    left = arr[:cur_len // 2]
    right = arr[cur_len // 2:]
    max_l = rec_find_max(left)
    max_r = rec_find_max(right)
    if max_l > max_r:
        return max_l
    else:
        return max_r

array = [1, 1000, 3, 4, 5, 6]
print(rec_find_max(array))