class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        result = 0
        # first and last digit
        a = [ int(str(n)[0])  for n in nums ]
        b = [ int(str(n)[-1]) for n in nums ]

        for i in range(len(a)):
            for j in range(i + 1, len(b)):
                if gcd(a[i], b[j]) == 1:
                    result += 1
        return result
