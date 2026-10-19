class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        result = []
        for i in nums:
            if nums.count(i) == 1:
                result.append(i)
            
        return sum(result)



        