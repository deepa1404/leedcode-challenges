class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = [c for c in s if c.isalpha()]
        chars.reverse()

        result = ""
        i = 0

        for c in s:
            if c.isalpha():
                result += chars[i]
                i += 1
            else:
                result += c

        return result