class Solution:
    def nearestPalindromic(self, n: str) -> str:
        size = len(n)
        if size == 1:
            return str(int(n) - 1)

        candidates = [ "9" * (size - 1) ] # largest palindrome with less digits
        candidates.append("1" + "0" * (size - 1) + "1")

        # round up
        half = (size + 1) // 2
        odd  = size % 2 == 1

        # first half
        first = int(n[:half])
        # change middle digit
        for i in range(first - 1, first + 2):
            one  = str(i)
            two  = one[:-1] if odd else one
            two  = two[::-1]
            if one + two != n:
                candidates.append(one + two)

        candidates.sort(key = lambda x : abs(int(x) - int(n)))
        return candidates[0]
