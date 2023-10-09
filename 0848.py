class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total  = 0
        result = []
        for i in range(len(s) - 1, -1, -1):
            total += shifts[i]
            total %= 26

            n  = ord(s[i]) - ord("a")
            n += total
            if n >= 26:
                n -= 26 # same as n % 26 but faster

            result.append(chr(n + ord("a")))

        return "".join(reversed(result))
