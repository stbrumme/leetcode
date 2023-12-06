class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        result = 0
        score  = -1
        seen   = set() # just a speed-run for repeated items
        for d in divisors:
            if d not in seen:
                current = 0
                for n in nums:
                    if n % d == 0:
                        current += 1
            seen.add(d)

            if score == current:
                result = min(result, d)
            if score <  current:
                score  = current
                result = d

        return result
