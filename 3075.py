class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        result = 0

        # pick most happy kids first
        wait = sorted(happiness, reverse = True)[ : k]
        for i, h in enumerate(wait):
            if i >= h: # early exit
                break
            result += h - i # some of them had to wait a little

        return result
