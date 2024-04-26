class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        size = len(words)

        for i in range(size):
            for j in range(i + 1, size):
                result += words[j].startswith(words[i]) and words[j].endswith(words[i])

        return result
