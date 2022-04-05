import math


def trailing_zeroes(n: int) -> int:
    answer = 0
    if n == 0:
        return answer
    for i in range(1, int(math.log(n, 5)) + 1):
        answer += (n // (5 ** i))
    return answer


if __name__ == '__main__':
    print(trailing_zeroes(30) == 7)
