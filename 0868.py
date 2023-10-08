class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)
        b = b[2:]        # strip "0b"
        b = b.strip("0") # no trailing zeros

        if b == "1":
            return 0 # only one set bit

        for result in range(len(b)):
            if b.find("0" * result) == -1:
                return result
