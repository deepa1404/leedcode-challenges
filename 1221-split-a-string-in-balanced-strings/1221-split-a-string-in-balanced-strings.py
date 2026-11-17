class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        start = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "R":
                balance += 1
            else:
                start += 1

            if balance == start and balance > 0:
                result += 1
               

        return result
        