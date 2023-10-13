class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = ""
        while a > 0 or b > 0:
            if result.endswith("aa"):
                result += "b"
                b -= 1
                continue

            if result.endswith("bb"):
                result += "a"
                a -= 1
                continue

            if a > b:
                result += "a"
                a -= 1
            else:
                result += "b"
                b -= 1

        return result
