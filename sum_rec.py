def rec_sum(arr):
    cur_len = len(arr)
    if cur_len == 1:
        return arr[0]
    left = arr[:cur_len // 2]
    right = arr[cur_len // 2:]
    return rec_sum(left) + rec_sum(right)

array = [1, 2, 3, 4, 5]
print(rec_sum(array))