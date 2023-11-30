class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result  = ""
        maximum = a + b + c
        for _ in range(maximum):
            recent = result[-2:]

            # avoid three identical letters
            if recent == "aa":
                if b > c:
                    result += "b"
                    b -= 1
                elif c > 0:
                    result += "c"
                    c -= 1
                continue

            if recent == "bb":
                if a > c:
                    result += "a"
                    a -= 1
                elif c > 0:
                    result += "c"
                    c -= 1
                continue

            if recent == "cc":
                if a > b:
                    result += "a"
                    a -= 1
                elif b > 0:
                    result += "b"
                    b -= 1
                continue

            # pick the letter with the highest allowed count
            high = max(a, b, c)
            if   a == high:
                result += "a"
                a -= 1
            elif b == high:
                result += "b"
                b -= 1
            elif c == high:
                result += "c"
                c -= 1

        return result
