class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        size = len(word)
        for result in range(1, size + 1):
            pos = result * k
            if pos >= size:
                break

            if word.startswith(word[pos :]):
                break

        return result
