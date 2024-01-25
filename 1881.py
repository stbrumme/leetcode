class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)

        if n[0] == "-":
            # negative => minimize number's absolute value
            for i, c in enumerate(n):
                if c > x:
                    return n[:i] + x + n[i:]
        else:
            # positive => maximize number's absolute value
            for i, c in enumerate(n):
                if c < x:
                    return n[:i] + x + n[i:]

        # best place is at the end
        return n + x
