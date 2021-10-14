import numpy as np


def ex_1():
    input = np.array([10, -13, 3, -6, -10, 41, -7, -6, -30, 34, -41, -15, 10, 1, 3, 13])
    sorted = np.sort(input)
    n = sorted.size

    quartile1 = (sorted[3] + sorted[4]) / 2
    quartile2 = (sorted[7] + sorted[8]) / 2
    quartile3 = (sorted[11] + sorted[12]) / 2

    interquartile = quartile3 - quartile1
    max_low = quartile1 - 1.5 * interquartile
    max_high = quartile3 + 1.5 * interquartile

    print(sorted)
    print(quartile1)
    print(quartile2)
    print(quartile3)
    print(interquartile)
    print(max_low)
    print(max_high)


def ex_3():
    input = np.array([1, 0, -4, 0, 2, 4, -1, 0, -3, 3, 4, 1, -4, -2, 0, 4])
    sorted = np.sort(input)
    n = sorted.size
    print(sorted)
    print(n)

def ex_6():
    input = np.array([5, 5, 3, 13, 4])
    print(input.mean())
    print(np.std(input))

ex_6()

