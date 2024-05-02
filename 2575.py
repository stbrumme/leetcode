class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        have = 0
        for c in word:
            have *= 10
            have += int(c)

            have %= m
            if have == 0:
                yield 1
            else:
                yield 0
