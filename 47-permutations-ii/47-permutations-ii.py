from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        uniqueset = set(list(permutations(nums, len(nums))))
        return [list(x) for x in uniqueset]
        