class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # parse complex number string
        def get(s):
            real, imaginary = s.split("+")
            return int(real), int(imaginary[: -1]) # strip "i", too

        r1, i1 = get(num1)
        r2, i2 = get(num2)

        #     num1    *   num2
        # = (r1 + i1*i) * (r2 + i2*i)
        # = r1*r2 + r1*i2*i + i1*r2*i + i1*i2*i*i   => i*i = -1
        # = r1*r2 - i1*i2 + i * (r1*i2 + i1*r2)
        r3 = r1 * r2 - i1 * i2
        i3 = r1 * i2 + i1 * r2

        return f"{r3}+{i3}i"
