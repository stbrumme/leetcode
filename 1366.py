class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = {}
        for c in votes[0]:
            teams[c] = 255 - ord(c) # reverse
        places = len(teams)

        for v in votes:
            for i, c in enumerate(v):
                shift = 10000**(1 + places - i)
                teams[c] += shift

        all = []
        for t in teams:
            all.append((teams[t], t))

        result = ""
        for score, name in sorted(all, reverse = True):
            result += name
        return result
