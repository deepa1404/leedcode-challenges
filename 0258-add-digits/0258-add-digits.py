class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                a = num % 10
                total += a
                num = num // 10
            num = total
        return num