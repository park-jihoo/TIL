import numpy as np
from typing import List


def shift_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    temp = np.reshape(np.roll(np.array(grid).flatten(), k), (len(grid), len(grid[0])))
    return temp


if __name__ == '__main__':
    print(shift_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
