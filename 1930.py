class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        all = dict()
        result = set()

        for letter in s:
            # third letter
            if letter in all:
                for middle in all[letter]:
                    result.add(letter + middle + letter)
            # second letter
            for first in all:
                all[first].add(letter)
            # first letter
            if not letter in all:
                all[letter] = set()

        return len(result)
