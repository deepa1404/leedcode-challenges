class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        n = columnNumber
        while n > 0:
            n -= 1
            remainder = n % 26
            result += chr(remainder + ord('A'))
            n //= 26

        return result[::-1]