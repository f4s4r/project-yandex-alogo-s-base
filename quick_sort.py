def quick_sort(array):
    cur_len = len(array)
    if cur_len < 2:
        return array
    print(array)
    p = array[0]
    lesser = [array[x] for x in range(cur_len) if array[x] < p]
    greater = [array[x] for x in range(cur_len) if array[x] > p]
    return quick_sort(lesser) + [p] + quick_sort(greater)
array = [5, 1, 6, 6, 42, 7, 8]
print(quick_sort(array))

