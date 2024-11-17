def max_sq(len_x, len_y):
    max_l, min_l = max(len_x, len_y), min(len_x, len_y)
    if max_l % min_l == 0:
        return min_l
    return max_sq(max_l % min_l, min_l)


x = 640
y = 400
print(max_sq(x, y))