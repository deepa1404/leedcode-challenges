class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                a = s[start:i + 1]
                if a == a[::-1]:
                    backtrack(i + 1, path + [a])

        backtrack(0, [])
        return res