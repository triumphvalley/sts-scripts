import numpy as np

def bravais_perason(x_in, y_in):
    x = np.array(x_in, dtype='f')
    x_mean = np.mean(x)
    print_row("x_i", x, x_mean)
    y = np.array(y_in, dtype='f')
    y_mean = np.mean(y)
    print_row("y_i", y, y_mean)
    x_2 = x ** 2
    x_2_mean = np.mean(x_2)
    print_row("x^2", x, x_mean)
    y_2 = y ** 2
    y_2_mean = np.mean(y_2)
    print_row("y^2", y, y_mean)
    xy = np.multiply(x, y)
    xy_mean = np.mean(xy)
    print_row("xy", xy, xy_mean)
    s_x_2 = x_2_mean - x_mean ** 2
    print(f"s_x_2 = {s_x_2:.4f}")
    s_x = s_x_2 ** 0.5
    print(f"s_x = {s_x:.4f}")
    s_y_2 = y_2_mean - y_mean ** 2
    print(f"s_y_2 = {s_y_2:.4f}")
    s_y = s_y_2 ** 0.5
    print(f"s_y = {s_y:.4f}")
    s_x_y = xy_mean - x_mean * y_mean
    print(f"s_x_y = {s_x_y:.4f}")
    r = s_x_y / (s_x * s_y)
    print(f"r = {r}")
    return r

def print_row(label, v, end):
    output = f"| {label:<5}"
    for el in v:
        output += f" | {el:10.2f}"
    output += f" | {end:10.2f} |"
    print(output)

def sperm_man_sort(arr_in):
    arr = np.array(arr_in, float)
    arr_sort = np.sort(arr)
    ranks = np.copy(arr)
    i = 0
    while i < len(arr_sort):
        indices = np.where(arr == arr_sort[i])[0]
        n_el = len(indices)
        rank = ((i + 1) + (i + n_el)) / 2
        for index in indices:
            arr[index] = rank
            ranks[index] = rank
        i += n_el
    return arr
    return ranks


print("Pearson")
pearson = bravais_perason(
     [5, 10, 20, 8, 4, 6, 12, 15],
     [27, 46, 73, 40, 30, 28, 47, 59]
)

print("Spearman")
spearman = bravais_perason(
     sperm_man_sort([5, 10, 20, 8, 4, 6, 12, 15]),
     sperm_man_sort([27, 46, 73, 40, 30, 28, 47, 59])
)


