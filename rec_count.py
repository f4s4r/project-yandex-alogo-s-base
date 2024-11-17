def rec_count(arr, cur_max):
    cur_len = len(arr)
    if cur_len == 1:
        return 1
    left = arr[:cur_len // 2]
    right = arr[cur_len // 2:]
    return rec_count(left) + rec_count(right)

array = [1, 2, 3, 4, 5, 6]
print(rec_count(array))