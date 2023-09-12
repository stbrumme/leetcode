class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        freq = defaultdict(int)
        for p in piles:
            freq[p] += 1

        guess = max(freq)
        while guess & (guess - 1): # round to next smaller power-of-two
            guess &= guess - 1
        step = guess // 2

        # round up
        def calc(k):
            return sum(freq[f] * (1 + (f - 1) // k) for f in freq)

        while step > 0:
            hours = calc(guess)

            # binary search
            if hours > h:
                guess += step
            else:
                guess -= step

            step //= 2

        # fine tuning
        while calc(guess) > h:
            guess += 1
        while guess > 1 and calc(guess - 1) <= h:
            guess -= 1

        return guess
