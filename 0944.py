class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0

        size = len(strs[0])
        for i in range(size):
            other = sorted(strs, key = lambda x : x[i])
            if strs != other:
                result += 1

        return result
