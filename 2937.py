class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # stop markers
        s1 += "#"
        s2 += "?"
        s3 += "!"

        # find length of common prefix
        for i in range(min(len(s1), len(s2), len(s3))):
            if s1[i] != s2[i] or s2[i] != s3[i]:
                break

        # minus one to remove the stop markers
        return -1 if i == 0 else (len(s1) - i - 1) + (len(s2) - i - 1) + (len(s3) - i - 1)
