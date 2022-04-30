from typing import List


def find_center(edges: List[List[int]]) -> int:
    a, b = edges[0][0], edges[0][1]
    if a in edges[1]:
        return a
    else:
        return b


if __name__ == '__main__':
    print(find_center([[1, 2], [2, 3], [4, 2]]))
