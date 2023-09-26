class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = defaultdict(set)
        for i in range(2, max(nums)+1):
            current = i
            # even numbers
            while (current & 1) == 0:
                factors[i].add(2)
                current >>= 1

            # odd numbers
            for j in range(3, i+1, 2):
                while current > 1 and current % j == 0:
                    factors[i].add(j)
                    current //= j

        all = set()
        for n in nums:
            all |= factors[n]

        return len(all)
