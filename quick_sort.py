import random as rnd
def quick_sort(array):
    cur_len = len(array)
    if cur_len < 2:
        return array
    print(array)
    p = array[rnd.randint(0, cur_len - 1)]
    lesser = [array[x] for x in range(cur_len) if array[x] < p]
    greater = [array[x] for x in range(cur_len) if array[x] > p]
    coefficient = 1 if len(lesser) + len(greater) == cur_len else cur_len - (len(lesser) + len(greater))
    return quick_sort(lesser) + [p] * coefficient + quick_sort(greater)
array = [5, 1, 6, 6, 42, 7, 8, 8, 8]
print(quick_sort(array))

