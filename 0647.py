class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        size = len(s)
        for i in range(size):
            # odd palindromes
            left = right = i
            result += 1
            while left > 0 and right < size - 1:
                left  -= 1
                right += 1
                if s[left] != s[right]:
                    break
                result += 1

            # even palindromes
            left  = i
            right = i + 1
            if right == size or s[left] != s[right]:
                continue

            result += 1
            while left > 0 and right < size - 1:
                left  -= 1
                right += 1
                if s[left] != s[right]:
                    break
                result += 1

        return result
