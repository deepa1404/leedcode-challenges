class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = max(nums)
        for i in range(len(nums)):
            if nums[i] == largest:
                a = i

        for num in nums:
            if num != largest and largest < 2 * num:
                return -1
        return a


            