class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        result = ""
        a = b = 0 # positions
        while a < len(word1) and b < len(word2):
            if word1[a:] > word2[b:]:
                result += word1[a]
                a += 1
            else:
                result += word2[b]
                b += 1

        return result + word1[a:] + word2[b:]
