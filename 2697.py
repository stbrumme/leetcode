class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        result = []

        left  = 0
        right = len(s) - 1
        # build minimum left half
        while left <= right:
            a = s[left]
            b = s[right]
            if a == b:
                result.append(a)
            else:
                result.append(min(a, b))

            left  += 1
            right -= 1

        # mirror
        if len(s) & 1:
            result += reversed(result[ : -1])
        else:
            result += reversed(result)

        return "".join(result)
