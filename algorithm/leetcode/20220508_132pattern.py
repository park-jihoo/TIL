from typing import List


def find132pattern(nums: List[int]) -> bool:
    m = float("-inf")
    stack = []
    for i in reversed(range(len(nums))):
        if nums[i] < m:
            return True
        else:
            while stack and nums[i] > stack[-1]:
                m = stack.pop()
            stack.append(nums[i])
    return False


if __name__ == '__main__':
    print(find132pattern([3, 1, 4, 2]))
