class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = nums[0], float('inf')
        for c in nums[1:]:
            if c > b:
                return True
            if c > a:
                b = c
            if c < a:
                a = c
        