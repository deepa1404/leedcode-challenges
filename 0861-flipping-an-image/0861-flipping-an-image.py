class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        result = []
        for row in image:
            new_row = []
            for i in row:
                if i == 1:
                    new_row.append(0)
                else:
                    new_row.append(1)
            result.append(new_row[::-1])
        return result

        