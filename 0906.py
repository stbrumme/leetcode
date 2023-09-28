class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left  = int(left)
        right = int(right)

        def ispalindrome(n):
            s = str(n)
            return s == s[::-1]

        result = 0
        for half in range(1, 22222+1): # sqrt(10^18) = 10^9, so one half has at most 5 digits
                                       # actually all digits seem always to be in [0,1,2], except for half=3
            s = str(half)

            odd  = int(s[:-1] + s[::-1])
            odd2 = odd * odd
            if left <= odd2 <= right and ispalindrome(odd2):
                result += 1

            if len(s) < 5: # len(s) == 5 yields 2*2*5=20 digits in the super-palindrome => too big
                even  = int(s + s[::-1])
                even2 = even * even
                if left <= even2 <= right and ispalindrome(even2):
                    result += 1

        return result
