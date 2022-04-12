from typing import List


def find_final_value(nums: List[int], original: int) -> int:
    for i in range(len(nums)):
        if original not in nums:
            return original
        original *= 2
    return original


if __name__ == '__main__':
    print(find_final_value([5, 3, 6, 1, 12], 3))
