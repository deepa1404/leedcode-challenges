class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        a, b = map(int, num1.replace('i', '').replace('+', ' ').split())
        c, d = map(int, num2.replace('i', '').replace('+', ' ').split())

        real = a*c - b*d
        imaginary = a*d + b*c

        return str(real) + "+" + str(imaginary) + "i"