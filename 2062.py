class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        for i in range(len(word)):
            have = set()
            for j in range(i, len(word)):
                if word[j] not in "aeiuo":
                    break
                have.add(word[j])
                if len(have) == 5:
                    result += 1
        return result
