class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            a = i**2
            ans.append(a)
        return sorted(ans)
        