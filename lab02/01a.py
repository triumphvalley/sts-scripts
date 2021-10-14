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
            ranks[index] = rank
        i += n_el
    return ranks

xy_input = [[8,7],[4,0],[2,-6],[1,4],[10,0],[-3,1],[-10,-3],[-4,5],[1,1],[-5,-3],[2,-2],[4,4],[-1,1],[6,-6]]
xy_values = np.array(xy_input)

x_values = xy_values[:, 0]
x_sorted = np.sort(x_values)
x_ranked = sperm_man_sort(x_values)
print(f"x-values: {list(x_values)}")
print(f"x-sorted: {list(x_sorted)}")
print(f"x-ranked: {list(x_ranked)}")
print("--------------------------------------------\n")

y_values = xy_values[:, 1]
y_sorted = np.sort(y_values)
y_ranked = sperm_man_sort(y_values)
print(f"y-values: {list(y_values)}")
print(f"y-sorted: {list(y_sorted)}")
print(f"y-ranked: {list(y_ranked)}")
print("--------------------------------------------\n")

print("Bravais Pearson")
bravais_perason(x_values, y_values)
print("--------------------------------------------\n")

print("Spearman")
bravais_perason(x_ranked, y_ranked)
print("--------------------------------------------\n")