class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        result = 1

        left = 0
        semi = 0
        for right in range(1, len(s)):
            # another pair
            if s[right] == s[right - 1]:
                semi += 1

            if semi <= 1:
                result = max(result, right - left + 1)
            else:
                # remove a pair
                while True:
                    left += 1
                    if s[left] == s[left - 1]:
                        semi -= 1
                        break

        return result
