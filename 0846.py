class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # card counter ...
        freq = defaultdict(int)
        for h in hand:
            freq[h] += 1

        for f in sorted(freq):
            # already processed
            if freq[f] == 0:
                continue

            # start a new group
            step = freq[f] # maybe multiple groups with the same cards
            for i in range(groupSize):
                freq[f + i] -= step
                # not consecutive ?
                if freq[f + i] < 0:
                    return False

        return True
