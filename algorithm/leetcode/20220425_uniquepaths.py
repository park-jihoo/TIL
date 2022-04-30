import math


def unique_paths(m: int, n: int):
    return (math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))) % (2 * 10 ** 9)


if __name__ == '__main__':
    print(unique_paths(3, 7))
