class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        # build in reverse order
        seq = [ deck.pop() ]
        while deck:
            seq.insert(0, seq.pop())
            seq.insert(0, deck.pop())
        return seq
