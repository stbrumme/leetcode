class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.leader = defaultdict(int)
        self.times  = times

        candidates = max(persons) + 1

        # current leader
        best  = 0
        votes = [ 0 ] * candidates
        for p, t in zip(persons, times):
            # add a vote
            votes[p] += 1
            # new leader (tie => most recent)
            if votes[best] <= votes[p]:
                best = p
            self.leader[t] = best

    def q(self, t: int) -> int:
        pos  = bisect_right(self.times, t) - 1
        when = self.times[pos]
        return self.leader[when]
