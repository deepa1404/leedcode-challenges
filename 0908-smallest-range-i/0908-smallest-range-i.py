class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        a = max(nums) - k
        b = min(nums) + k
        c = a - b
        return max(0,c)
           