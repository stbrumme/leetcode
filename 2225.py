class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        lost = defaultdict(int)
        for m in matches:
            lost[m[1]] += 1
            players.add(m[0])
            players.add(m[1])

        p = sorted(players)

        perfect = [ i for i in p if lost[i] == 0 ]
        one     = [ i for i in p if lost[i] == 1 ]
        return [ perfect, one ]
