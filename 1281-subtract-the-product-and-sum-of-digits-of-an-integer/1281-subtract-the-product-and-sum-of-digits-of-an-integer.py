class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = 1
        a = sum(map(int,str(n)))
        for i in str(n):
            res *= int(i)
        return res - a


       