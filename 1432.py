class Solution:
    def maxDiff(self, num: int) -> int:
        def replace(n, x, y):
            s = str(n).replace(str(x), str(y))
            return n if s[0] == "0" else int(s)

        # nothing smart here ...
        result = 0
        for x in range(10):
            for y in range(10):
                a = replace(num, x, y)
                for x2 in range(10):
                    for y2 in range(10):
                        b = replace(num, x2, y2)
                        if a != 0 and b != 0:
                            result = max(result, abs(a - b))

        return result
