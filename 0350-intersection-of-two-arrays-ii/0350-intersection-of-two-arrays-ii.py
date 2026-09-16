from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
       a = Counter(nums1)
       b = Counter(nums2)
       result = []

       for num in a:
        result.extend([num] * min(a[num], b[num]))
       return result
    



    

      