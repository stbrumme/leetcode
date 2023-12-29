class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        result = ""
        for c in s:
            result += c
            while len(result) >= k          and \
                  result[-k]  == result[-1] and \
                  result[-k:] == result[-1] * k:
                result = result[:-k]

        return result
