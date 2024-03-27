class Solution:
    def largestPalindrome(self, n: int) -> int:
        # cheating possible:
        # only 8 valid inputs, just create 8 test cases and write down the results ...

        # by trial'n'error I saw that the palindrome has always 2n digits (except when n = 1)
        if n == 1:
            return 9 # 1 * 9 = 9 % 1337

        high = int("9" * n)     # e.g. n = 3: 999
        for current in range(high, 0, -1):
            # create palindrome
            s = str(current)
            palindrome = int(s + s[::-1])

            for factor in range(current | 1, high, 2): # factors are always odd, therefore +2
                if palindrome % factor == 0 and palindrome // factor <= high:
                    return palindrome % 1337
