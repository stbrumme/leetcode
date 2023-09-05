class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ""
        all = set(words)
        for w in words:
            if len(w) < len(result):
                continue

            shorter = w
            while shorter in words:
                shorter = shorter[:-1]
            if shorter:
                continue

            if len(w) > len(result):
                result = w
            else:
                result = min(result, w)

        return result
