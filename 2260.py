class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        result = +inf

        size = len(cards)
        have = {}

        for i, current in enumerate(cards):
            # shrink sliding window until no matching cards anymore
            if current in have:
                start = i - len(have)
                end   = have[current]
                for remove in cards[start : end]:
                    del have[remove]
                result = min(result, len(have) + 1)

            have[current] = i

        return result if result != +inf else -1
