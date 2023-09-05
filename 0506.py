class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        places = sorted(score)

        for s in score:
            pos = len(score) - bisect_left(places, s)
            if pos == 1:
                yield "Gold Medal"
            elif pos == 2:
                yield "Silver Medal"
            elif pos == 3:
                yield "Bronze Medal"
            else:
                yield str(pos)
