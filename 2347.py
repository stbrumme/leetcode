class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        freq = [ 0 ] * 14
        for r in ranks:
            freq[r] += 1

        same = max(freq)
        if same >= 3:
            return "Three of a Kind"
        if same == 2:
            return "Pair"

        return "High Card"
