from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    return [x[0] for x in counter.most_common(k)]


if __name__ == '__main__':
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2])
